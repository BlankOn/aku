# Django settings for aku project.

import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

ADMINS = (('Fitra Aditya', 'aditya.fp@gmail.com'), )

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',
        'NAME': 'aku.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Asia/Jakarta'

LANGUAGE_CODE = 'id'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.normpath(os.path.join(PROJECT_PATH, 'media'))

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = '!(p&y-8f6gdtdfzn7qp7f0b+yw*l+)caeept1rl7v$zqaz7o23'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader', )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware', )

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, 'templates'), )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django_openid_auth',
    'openid_provider',
    'auth',
    'profile', )

DEFAULT_AVATAR = os.path.join(MEDIA_ROOT, 'generic.jpg')
GRAVATAR = False

AVATAR_WEBSEARCH = True

# 127.0.0.1:8000 Google Maps API Key
GOOGLE_MAPS_API_KEY = ""

AUTH_PROFILE_MODULE = 'profile.profile'

DEFAULT_FROM_EMAIL = 'username@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'username@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = True

ACCOUNT_ACTIVATION_DAYS = 3
LOGIN_REDIRECT_URL = '/'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
