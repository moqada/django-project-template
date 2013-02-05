# -*- coding: utf-8 -*-
from {{ project_name }}.settings.common import *


# for debug
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# for Email
MANAGERS = (
    ('Your Production Name', 'your_production_email@example.com'),
)
SERVER_EMAIL = 'your_production_server_email@example.com'

# import local settings
try:
    from .local import *
except ImportError:
    pass
