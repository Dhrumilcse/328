from settings import PROJECT_ROOT, SITE_ROOT
import os

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shop',
        'USER' : 'dhrumil',
        'PASSWORD' : '14co33@shop',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}