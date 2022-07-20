################################################################################

# pip install dj-database-url
# pip install python-dotenv
# pip install whitenoise
# pip install django-cors-headers
# pip install djangorestframework

import dj_database_url  # noqa: E402

from dotenv import load_dotenv  # noqa: E402
from urllib import parse  # noqa: E402
from django.contrib import messages  # noqa: E402

#  autoload the env vars in .env file
load_dotenv(BASE_DIR / '.env')


#  function to get environment variables in proper format
def getenv(name: str, default=None):
    import os  # noqa: E402
    value: str = os.getenv(name)
    if value is None:
        return default
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.isdecimal():
        return int(value)
    return default


SITE_NAME = getenv('SITE_NAME', "http://127.0.0.1")
DEBUG = getenv("DJANGO_DEBUG", DEBUG)
SECRET_KEY = getenv('SECRET_KEY', SECRET_KEY)
if not DEBUG:
    #  noinspection SpellCheckingInspection
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = [""]
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    ALLOWED_HOSTS = [parse.urlsplit(SITE_NAME).hostname, ]
    CORS_ALLOWED_ORIGINS = ["https://" + str(host) for host in ALLOWED_HOSTS]
else:
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_CREDENTIALS = True
    ALLOWED_HOSTS = ['*', ]

#  change default class tags for message passed to page
MESSAGE_TAGS = {
    messages.DEBUG: 'dark debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger error',
}

#  cache storage setup, DatabaseCache by default
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
        'TIMEOUT': 500,
        'OPTIONS': {
            'MAX_ENTRIES': 10,
            'CULL_FREQUENCY': 1,
        },
    }
}

MIDDLEWARE += [
    #  data flair caching middlewares
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',

    #  cross-origin resource sharing header setup middleware
    'corsheaders.middleware.CorsMiddleware',

    #  whitenoise middleware for static files serving
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

INSTALLED_APPS += [
    'rest_framework',
    'corsheaders',
]
AUTHENTICATION_BACKENDS = [
    # Needed to log in by username in Django admin, regardless of any other backend
    'django.contrib.auth.backends.ModelBackend',
]

#  root template dirs
TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates', ]

#  template context processors
TEMPLATES[0]['OPTIONS']['context_processors'] += []

#  Configuration for serving static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#  extra dirs to store static files
STATICFILES_DIRS = []

#  url path to serve static files from
STATIC_URL = "/static/"

#  default dir to store collected static files
STATIC_ROOT = BASE_DIR / 'static'

#  default dir to store uploaded media
MEDIA_ROOT = BASE_DIR / 'media'

#  url path to serve media files
MEDIA_URL = '/media/'

#  configuration to manage email service
EMAIL_BACKEND = getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_USE_TLS = getenv("EMAIL_USE_TLS", True)
EMAIL_HOST = getenv('EMAIL_HOST')
EMAIL_PORT = getenv('EMAIL_PORT')
EMAIL_HOST_USER = getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = getenv('EMAIL_HOST_PASSWORD')


ADMIN_URL = getenv('ADMIN_URL', 'administration')
LOGIN_REDIRECT_URL = '/'
DATABASES['default'] = dj_database_url.config(default="sqlite:///database.db", conn_max_age=600, ssl_require=False)

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_AUTHENTICATION_CLASSES': [
    ],
}

JWT_DEFAULTS = {
    "Algorithm": getenv('JWT_ALGORITHM', 'HS256'),
    "Secret": getenv('JWT_SECRET', SECRET_KEY),
    "Issuer": getenv('JWT_ISSUER', SITE_NAME),
    "MaxLife": getenv('JWT_MAX_LIFE', 90000),
}
