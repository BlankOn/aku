from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template

from auth.views import get_profiles

admin.autodiscover()

urlpatterns = patterns(
    '',
    # static page
    (r'^$', direct_to_template, {
        'extra_context': {
            'profiles': get_profiles
        },
        'template': 'front.html'
    }),
    (r'^privacy.html', direct_to_template, {
        'template': 'privacy.html'
    }),
    # dynamic page
    url(r'^o/', include('openid_provider.urls')),
    url(r'^accounts/', include('auth.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^media/(?P<path>.*)', 'django.views.static.serve', {
        'document_root': 'media'
    }), )
