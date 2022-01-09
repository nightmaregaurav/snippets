# Additional Settings
import os  # noqa: E402
import sys  # noqa: E402
from django.contrib import messages  # noqa: E402
from urllib import parse  # noqa: E402
from dotenv import load_dotenv

# autoload the env vars in .env file
project_folder = os.path.expanduser(BASE_DIR)
load_dotenv(BASE_DIR / '.env')

# add site name to env variable first
SITE_NAME = os.getenv('SITE_NAME')

# noinspection PyRedeclaration
DEBUG = os.getenv('DJANGO_DEBUG') == "True"
if not DEBUG:
    # add secret key to env variable first
    SECRET_KEY = os.getenv('SECRET_KEY')
    ALLOWED_HOSTS = [parse.urlsplit(SITE_NAME).hostname, ]
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    # noinspection SpellCheckingInspection
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
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
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table'
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

# Database in mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_DB_NAME'),
        'USER': os.getenv('MYSQL_DB_USER'),
        'PASSWORD': os.getenv('MYSQL_DB_PASS'),
        'HOST': os.getenv('MYSQL_DB_HOST'),
        'PORT': os.getenv('MYSQL_DB_PORT'),
        'TIME_ZONE': os.getenv('MYSQL_DB_TIME_ZONE'),
    }
}


AUTHENTICATION_BACKENDS = [
    # Needed to log in by username in Django admin, regardless of any other backend
    'django.contrib.auth.backends.ModelBackend',
]
LOGIN_REDIRECT_URL = '/'

MIDDLEWARE += []

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
