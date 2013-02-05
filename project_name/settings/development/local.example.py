# -*- coding: utf-8 -*-
from . import *


# database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'DATABASE_NAME',               # Or path to database file if using sqlite3.
        'USER': 'DATABASE_USER',               # Not used with sqlite3.
        'PASSWORD': 'DATABASE_PASSWORD',       # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
