# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 : */

from django.contrib import admin

from models import TrustedRoot, OpenID


class TrustedRootInline(admin.TabularInline):
    model = TrustedRoot


class OpenIDAdmin(admin.ModelAdmin):
    list_display = ['user', 'openid']
    inlines = [TrustedRootInline, ]


admin.site.register(OpenID, OpenIDAdmin)
