from .common import *

DEBUG = False

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY)

DATABASES = {
    'default' : {
        'ENGINE': os.environ.get('DJANGO_DATABASE_ENGINE', 'django.db.backends.postresql_psycopg2'),
        'NAME': os.environ.get('DJANGO_DATABASE_ENGINE', 'ubuntu'),
        'USER': os.environ.get('DJANGO_DATABASE_NAME', 'ubuntu'),
        'PASSWORD': os.environ.get('DJANGO_DATABASE_PASSWORD', 'withaskdjango!'),
        'HOST': os.environ.get('DJANGO_DATABAS_HOST', '127.0.0.1'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')
MEDIA_URL = '/media/'