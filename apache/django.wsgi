import os
import sys
#import site
#import platform

VIRTUALENV_PATH = '/home/django/.virtualenvs/django-1.6.7/'
SOURCE_ROOT_PATH = '/home/django/source/bhp045/'
LOCAL_PROJECT_RELPATH = 'bhp045_project/bhp045/'

# Add the site-packages of the chosen virtualenv to work with

# update path
sys.path.insert(0, os.path.join(VIRTUALENV_PATH, 'local/lib/python2.7/site-packages'))
sys.path.insert(0, os.path.join(SOURCE_ROOT_PATH, 'edc_project'))
sys.path.insert(0, os.path.join(SOURCE_ROOT_PATH, 'lis_project'))
sys.path.insert(0, os.path.join(SOURCE_ROOT_PATH, LOCAL_PROJECT_RELPATH))
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
#if platform.system() == 'Darwin':
#        os.environ['PYTHON_EGG_CACHE'] = '/usr/local/pylons/python-eggs'
# Activate the virtual env
activate_env=os.path.join(VIRTUALENV_PATH, 'bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
