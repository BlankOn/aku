from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from profile.models import SSHKeys
from subprocess import Popen, PIPE
import tempfile
import os

attrs_dict = { 'class': 'required' }

class SSHKeysForm(forms.Form):
    deleting = False
    success = False
    fingerprint = forms.CharField(widget=forms.HiddenInput)
    key = forms.CharField(widget=forms.Textarea(attrs=dict(attrs_dict, cols=80, rows=5)))
    def clean(self):
        return self.cleaned_data
    def delete(self, user):
        self.deleting = True
        try:
            keyring = SSHKeys.objects.get(user=user, fingerprint=self.data['fingerprint'])  
            keyring.delete()
            self.success = True
        except Exception as e:
            pass

class SSHKeyUploadForm(forms.Form):
    file = forms.FileField(_('choose file'))
    text = ""
    fingerprint = ""
    success = False
    saving = False
    def clean(self):
        return self.cleaned_data
    def clean_file(self):
        if self.files['file'].size > 1024:
            raise forms.ValidationError(_("The file you uploaded ('%s') is too big" % self.files['file']))
        (fd, file) = tempfile.mkstemp(prefix='irgsh-sshkeys-')
        f = os.fdopen(fd, 'w')
        for chunk in self.files['file'].chunks():
            self.text += chunk
            f.write(chunk)
        f.close()
        output = Popen(["ssh-vulnkey", "-v", file], stdout=PIPE).communicate()[0]
        state = 0
        for line in output.split("\n"):
            if line.startswith(file):
                state = 1
                fields = line.split(": ")
                self.fingerprint = fields[2].split(" ")[2]
                if line.find("COMPROMISED") != -1:
                    state = 2
        os.remove(file)
        if state == 0 or self.fingerprint == "":
            raise forms.ValidationError(_("The file you uploaded ('%s') is not a valid SSH key file" % self.files['file']))
        if state == 2:
            raise forms.ValidationError(_("The file you uploaded ('%s') is a compromised SSH key file. Replace it immediately" % self.files['file']))
        return self.cleaned_data['file']
    def save(self, user):
        keyring = SSHKeys(user=user, fingerprint=self.fingerprint, key=self.text)  
        try:
            self.saving = True
            keyring.save()
            self.success = True
        except Exception:
            pass
