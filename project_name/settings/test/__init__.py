# -*- coding: utf-8 -*-
from {{ project_name }}.settings.common import *

# using in-memory database
DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = ':memory:'

# does not run migrate
SOUTH_TESTS_MIGRATE = False

# import local settings
try:
    from .local import *
except ImportError:
    pass
