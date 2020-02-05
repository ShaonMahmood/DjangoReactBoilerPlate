from .base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'ip-address', 'your-website.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your-db-name',
        'USER': 'your-db-user-name',
        'PASSWORD': 'your-db-password',
        'HOST': 'your-db-host',
        'PORT': '',
    }
}