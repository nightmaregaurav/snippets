# Additional Settings
import os  # noqa: E402
import sys  # noqa: E402
import dj_database_url  # noqa: E402

from django.contrib import messages  # noqa: E402
from urllib import parse  # noqa: E402
from dotenv import load_dotenv  # noqa: E402

# autoload the env vars in .env file
load_dotenv(BASE_DIR / '.env')

# add site name to env variable first
SITE_NAME = os.getenv('SITE_NAME')

# noinspection PyRedeclaration
DEBUG = os.getenv('DJANGO_DEBUG') == "True"
if not DEBUG:
    # add secret key to env variable first
    SECRET_KEY = os.getenv('SECRET_KEY')
    ALLOWED_HOSTS = [parse.urlsplit(SITE_NAME).hostname, *os.getenv('ALLOWED_HOSTS').split()]
    SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE') or True
    SECURE_BROWSER_XSS_FILTER = os.getenv('SECURE_BROWSER_XSS_FILTER') or True
    # noinspection SpellCheckingInspection
    SECURE_CONTENT_TYPE_NOSNIFF = os.getenv('SECURE_CONTENT_TYPE_NOSNIFF') or True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = os.getenv('SECURE_HSTS_INCLUDE_SUBDOMAINS') or True
    SECURE_HSTS_SECONDS = os.getenv('SECURE_HSTS_SECONDS') or 31536000
    SECURE_REDIRECT_EXEMPT = [*os.getenv('SECURE_REDIRECT_EXEMPT').split()]
    SECURE_SSL_REDIRECT = os.getenv('SECURE_SSL_REDIRECT') or True
    SECURE_PROXY_SSL_HEADER = os.getenv('SECURE_PROXY_SSL_HEADER').split() or ('HTTP_X_FORWARDED_PROTO', 'https')
else:
    ALLOWED_HOSTS = ['*', ]

# noinspection SpellCheckingInspection
INSTALLED_APPS += ['Core.apps.CoreConfig',
                   ]

TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates', ]
TEMPLATES[0]['OPTIONS']['context_processors'] += [
    'Core.modules.context_processors.urls',
    'Core.modules.context_processors.site_setting',
]

CACHES = {
    'default': {
        'BACKEND': os.getenv('CACHE_BACKEND') or 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': os.getenv('CACHE_LOCATION') or 'cache_table'
    }
}

MESSAGE_TAGS = {
    messages.DEBUG: 'dark debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger error',
}

STATICFILES_DIRS = [BASE_DIR / 'static_files']
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

AUTHENTICATION_BACKENDS = [
    # Needed to log in by username in Django admin, regardless of any other backend
    'django.contrib.auth.backends.ModelBackend',
]
LOGIN_REDIRECT_URL = '/'

MIDDLEWARE += []

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND') or 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS') or True
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


#  Configuration for serving static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Database configuration
DATABASES['default'] = dj_database_url.config(default="sqlite:///database.db", conn_max_age=600, ssl_require=True)
