# Create your admin here.
"""
Admin configuration for Aku authentication
"""

from django.contrib import admin

from auth.models import Avatar, EmailValidation


class EmailValidationAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', )
    search_fields = ('user__username', 'user__first_name')


admin.site.register(Avatar)
admin.site.register(EmailValidation, EmailValidationAdmin)
