#######################
Django Project Template
#######################

Install for development
=======================

1. startproject
---------------

.. code::
   django-admin.py startproject --template=https://github.com/moqada/django-project-template/zipball/master project_name

2. pip install
--------------

.. code::
   cd project_name
   pip install requirements/development.txt

4. Edit local settings
----------------------

If you have local settings per a developer.

.. code::
   cp project_name/settings/development/local.example.py project_name/settings/development/local.py

3. syncdb
---------

.. code::
   python manage.py syncdb --settings=project_name.settings.development

5. runserver
------------

.. code::
   python manage.py runserver --settings=project_name.settings.development
