# Additional Settings
# pip install dj-database-url
# pip install python-dotenv
# pip install whitenoise
import os  # noqa: E402
import sys  # noqa: E402
import dj_database_url  # noqa: E402
import json  # noqa: E402

from django.contrib import messages  # noqa: E402
from urllib import parse  # noqa: E402
from dotenv import load_dotenv  # noqa: E402


def get_bool_or_default_env_var(name: str, default: bool):
    str_value: str = os.getenv(name)

    if str_value is None:
        return default

    str_value = str_value.lower()

    if str_value == "true":
        return True
    if str_value == "false":
        return False
    return default


# autoload the env vars in .env file
load_dotenv(BASE_DIR / '.env')

# add site name to env variable first
SITE_NAME = os.getenv('SITE_NAME')

# noinspection PyRedeclaration
DEBUG = get_bool_or_default_env_var("DJANGO_DEBUG", True)
if not DEBUG:
    # add secret key to env variable first
    SECRET_KEY = os.getenv('SECRET_KEY')
    ALLOWED_HOSTS = [parse.urlsplit(SITE_NAME).hostname, *os.getenv('ALLOWED_HOSTS').split()]
    SESSION_COOKIE_SECURE = get_bool_or_default_env_var("SESSION_COOKIE_SECURE", True)
    SECURE_BROWSER_XSS_FILTER = get_bool_or_default_env_var("SECURE_BROWSER_XSS_FILTER", True)
    # noinspection SpellCheckingInspection
    SECURE_CONTENT_TYPE_NOSNIFF = get_bool_or_default_env_var("SECURE_CONTENT_TYPE_NOSNIFF", True)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = get_bool_or_default_env_var("SECURE_HSTS_INCLUDE_SUBDOMAINS", True)
    SECURE_HSTS_SECONDS = os.getenv('SECURE_HSTS_SECONDS') or 31536000
    SECURE_REDIRECT_EXEMPT = [*os.getenv('SECURE_REDIRECT_EXEMPT').split()]
    SECURE_SSL_REDIRECT = get_bool_or_default_env_var("SECURE_SSL_REDIRECT", True)
    SECURE_PROXY_SSL_HEADER = os.getenv('SECURE_PROXY_SSL_HEADER').split() or ('HTTP_X_FORWARDED_PROTO', 'https')
else:
    ALLOWED_HOSTS = ['*', ]

# root template dirs
TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates', ]

# change default tags for message passed to page
MESSAGE_TAGS = {
    messages.DEBUG: 'dark debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger error',
}

# default dir to store collected static files
STATICFILES_DIRS = [BASE_DIR / 'static_files']

# dirs to store root static files
STATIC_ROOT = BASE_DIR / 'static'

# url path to serve media files
MEDIA_URL = '/media/'

# default dir to store uploaded media
MEDIA_ROOT = BASE_DIR / 'media'

# url that users will be redirected to after login
LOGIN_REDIRECT_URL = '/'

# cache storage setup, DatabaseCache by default
CACHES = {
    'default': {
        'BACKEND': os.getenv('CACHE_BACKEND') or 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': os.getenv('CACHE_LOCATION') or 'cache_table',
        'TIMEOUT': os.getenv('CACHE_TIMEOUT') or 500,
        'OPTIONS': {
            'MAX_ENTRIES': os.getenv('CACHE_MAX_ENTRIES') or 10,
            'CULL_FREQUENCY': os.getenv('CACHE_CULL_FREQUENCY') or 1,
        },
    }
}

# DataFlair caching middlewares
MIDDLEWARE += [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

# configuration to manage email service
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND') or 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = get_bool_or_default_env_var("EMAIL_USE_TLS", True)
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

#  Configuration for serving static files storage using whitenoise by default
STATICFILES_STORAGE = os.getenv('STATICFILES_STORAGE') or 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# database configuration using sqlite by default
DATABASES['default'] = dj_database_url.config(default="sqlite:///database.db", conn_max_age=600, ssl_require=False)

# auth backends
AUTHENTICATION_BACKENDS = [
    # Needed to log in by username in Django admin, regardless of any other backend
    'django.contrib.auth.backends.ModelBackend',
]

# template context processors
TEMPLATES[0]['OPTIONS']['context_processors'] += [
    'Core.modules.context_processors.urls',
    'Core.modules.context_processors.site_setting',
]

# noinspection SpellCheckingInspection
INSTALLED_APPS += [
    'Core.apps.CoreConfig',
]

# middlewares
MIDDLEWARE += [
]
