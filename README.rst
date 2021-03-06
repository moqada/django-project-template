#######################
Django Project Template
#######################

Install for development
=======================

1. startproject
---------------

::

   django-admin.py startproject --template=https://github.com/moqada/django-project-template/zipball/master project_name

2. pip install
--------------

::

   cd project_name
   pip install requirements/development.txt

4. Edit local settings
----------------------

If you have local settings per a developer.

::

   cp project_name/settings/development/local.example.py project_name/settings/development/local.py

3. syncdb
---------

::

   python manage.py syncdb --settings=project_name.settings.development

5. runserver
------------

::

   python manage.py runserver --settings=project_name.settings.development


Other usage
===========

For Test
--------

::

   python manage.py test <app_name> --settings=project_name.settings.test

For Jenkins
-----------

::

   pip install -r requirements/jenkins.txt
   python manage.py jenkins --settings=project_name.settings.test.jenkins
