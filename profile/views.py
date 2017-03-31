# Create your views here.

from profile.forms import SSHKeysForm, SSHKeyUploadForm
from profile.models import SSHKeys

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


@login_required
def manage_ssh_key(request):
    keys = SSHKeys.objects.filter(user=request.user)
    context = RequestContext(request)
    return render_to_response("userprofile/profile/sshkeys_manage.html",
                              {'keys': keys}, context_instance=context)


@login_required
def delete_ssh_key(request, key=None):
    if request.method == 'POST':
        form = SSHKeysForm(data=request.POST, files=request.FILES)
        key = request.POST['fingerprint']
        form.delete(request.user)
    else:
        try:
            entry = SSHKeys.objects.get(user=request.user, fingerprint=key)
            data = {'user': request.user, 'fingerprint': key, 'key': entry.key}
        except:
            key = None
            data = {'user': request.user, 'key': None}
        form = SSHKeysForm(data)

    context = RequestContext(request)
    return render_to_response("userprofile/profile/sshkeys_delete.html",
                              {'key': key, 'form': form},
                              context_instance=context)


@login_required
def upload_ssh_key(request):
    if request.method == 'POST':
        form = SSHKeyUploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse('manage_ssh_key'))
    else:
        form = SSHKeyUploadForm()

    context = RequestContext(request)
    return render_to_response("userprofile/profile/sshkeys_upload.html",
                              {'form': form}, context_instance=context)
