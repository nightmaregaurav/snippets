# Additional Settings
import os
import sys
from django.contrib import messages

# noinspection PyRedeclaration
DEBUG = os.getenv('DJANGO_DEBUG') == "True"

if not DEBUG:
    # add secret key to env variable first
    SECRET_KEY = os.getenv('SECRET_KEY')
    # add your domain name(s) here
    ALLOWED_HOSTS = []
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
else:
    ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ['Core.apps.CoreConfig']

TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates', ]
TEMPLATES[0]['OPTIONS']['context_processors'] += [
    'Core.modules.context_processors.urls',
    'Core.modules.context_processors.site_setting',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table'
    }
}

MESSAGE_TAGS = {
    messages.DEBUG: 'dark',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

STATICFILES_DIRS = [BASE_DIR / 'static_files']
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

LOGIN_REDIRECT_URL = '/'

# Database in mysql change data as required
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ere',
        'USER': 'pma',
        'PASSWORD': 'pma',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}