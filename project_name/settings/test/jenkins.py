# -*- coding: utf-8 -*-
from {{ project_name }}.settings.test import *

# django-jenkins
INSTALLED_APPS += ('django_jenkins',)
PROJECT_APPS = (
    'APP_NAME',
)
# @see: https://github.com/kmmbvnr/django-jenkins/blob/master/README.rst
JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.django_tests',
    'django_jenkins.tasks.run_jshint',
    'django_jenkins.tasks.run_csslint',
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
    #'django_jenkins.tasks.run_flake8',
    #'django_jenkins.tasks.run_sloccount',
    'django_jenkins.tasks.lettuce_tests',
)

# import local settings
try:
    from .local import *
except ImportError:
    pass
