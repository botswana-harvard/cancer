import os
import sys
import socket

from unipath import Path

from .installed_apps import DJANGO_APPS, THIRD_PARTY_APPS, EDC_APPS, LOCAL_APPS
from .cancer_settings import (APP_NAME, PROJECT_NUMBER, PROJECT_IDENTIFIER_PREFIX,
                              PROJECT_IDENTIFIER_MODULUS, PROTOCOL_REVISION, INSTITUTION)
from .databases import TESTING_SQLITE, TESTING_MYSQL, PRODUCTION_MYSQL
from .device import SITE_CODE, DEVICE_ID
from .mail_settings import (EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER,
                            EMAIL_HOST_PASSWORD, EMAIL_USE_TLS)

DEBUG = True  # Note: should be False for collectstatic
TEMPLATE_DEBUG = DEBUG
ADMINS = (('erikvw', 'ew@2789@gmail.com'),
          ('mkewagamang', 'mkewagamang@bhp.org.bw'),)

APP_NAME = APP_NAME

# PATHS
DIRNAME = os.path.dirname(os.path.abspath(__file__))  # needed??
SOURCE_ROOT = Path(os.path.dirname(os.path.realpath(__file__))).ancestor(3)  # e.g. /home/django/source
EDC_DIR = SOURCE_ROOT.child('edc_project').child('edc')  # e.g. /home/django/source/edc_project/edc
TEMPLATE_DIRS = (
    EDC_DIR.child('templates'),
)
PROJECT_ROOT = Path(os.path.dirname(os.path.realpath(__file__))).ancestor(2)  # e.g. /home/django/source/bhp066_project
PROJECT_DIR = Path(os.path.dirname(os.path.realpath(__file__))).ancestor(1)  # e.g. /home/django/source/bhp066_project/bhp066
APP_DIR = PROJECT_DIR.child('apps').child(APP_NAME)  # e.g. /home/django/source/bhp066_project/bhp066/apps/bcpp
ETC_DIR = PROJECT_DIR.child('config').child('etc')  # for production this should be /etc/edc
STATIC_ROOT = PROJECT_DIR.child('static')
FIXTURE_DIRS = (
    APP_DIR.child('fixtures'),
)
STATICFILES_DIRS = ()
CONFIG_DIR = PROJECT_DIR.child('config')

# edc.crytpo_fields encryption keys
# developers should set by catching their hostname instead of setting explicitly
if socket.gethostname() == 'mac.local':
    KEY_PATH = '/Volumes/bhp066/live_keys'  # DONT DELETE ME!!, just comment out
elif socket.gethostname() == 'silverapple':
    KEY_PATH = '/Users/melissa/Documents/git/source/bhp045_project/bhp045/keys'
else:
    KEY_PATH = PROJECT_DIR.child('keys')  # DONT DELETE ME!!, just comment out
    #KEY_PATH = '/Volumes/keys'  # DONT DELETE ME!!, just comment out

MANAGERS = ADMINS

# DATABASES
CONN_MAX_AGE = 15
testing_db_name = 'sqlite'
if 'test' in sys.argv:
    # make tests faster
    SOUTH_TESTS_MIGRATE = False
    if testing_db_name == 'sqlite':
        DATABASES = TESTING_SQLITE
    else:
        DATABASES = TESTING_MYSQL
else:
    DATABASES = PRODUCTION_MYSQL

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Africa/Gaborone'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
# langauage setting

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

LANGUAGE_CODE = 'en'

SITE_ID = 1

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL that handles the static files served from STATIC_ROOT.
STATIC_URL = '/static/'

# A list of locations of additional static files
STATICFILES_DIRS = ()

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
)

# Make this unique, and don't share it with anybody.
with open(os.path.join(ETC_DIR, 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
     'django.template.loaders.filesystem.Loader',
     'django.template.loaders.app_directories.Loader',
     'django.template.loaders.eggs.Loader',
     )),
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.request",
                               "django.contrib.messages.context_processors.messages",
                               )

ROOT_URLCONF = 'config.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'config.wsgi.application'

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + EDC_APPS + LOCAL_APPS  # + ('django_nose', )

# django
SESSION_COOKIE_AGE = 10000
SHORT_DATE_FORMAT = 'Y-m-d'
SHORT_DATETIME_FORMAT = 'Y-m-d H:i'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# django email settings
EMAIL_HOST = EMAIL_HOST
EMAIL_PORT = EMAIL_PORT
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = EMAIL_USE_TLS
# EMAIL_AFTER_CONSUME = False

# django auth
AUTH_PROFILE_MODULE = "bhp_userprofile.userprofile"

# general
PROJECT_NUMBER = PROJECT_NUMBER
PROJECT_IDENTIFIER_PREFIX = PROJECT_IDENTIFIER_PREFIX
PROJECT_IDENTIFIER_MODULUS = PROJECT_IDENTIFIER_MODULUS
PROTOCOL_REVISION = PROTOCOL_REVISION
INSTITUTION = INSTITUTION

# admin overrides
LOGIN_URL = '/{app_name}/login/'.format(app_name=APP_NAME)
LOGIN_REDIRECT_URL = '/{app_name}/'.format(app_name=APP_NAME)
LOGOUT_URL = '/{app_name}/logout/'.format(app_name=APP_NAME)

# south
SOUTH_LOGGING_FILE = os.path.join(os.path.dirname(__file__), "south.log")
SOUTH_LOGGING_ON = True

# dajax
DAJAXICE_MEDIA_PREFIX = "dajaxice"

# edc.subject.registered_subject
SUBJECT_APP_LIST = ['cancer_subject']
SUBJECT_TYPES = ['subject']
MAX_SUBJECTS = {'subject': 4000, }

# edc.crypto_fields
IS_SECURE_DEVICE = False
MAY_CREATE_NEW_KEYS = True
FIELD_MAX_LENGTH = 'migration'

# edc.map
SITE_CODE = SITE_CODE

ALLOW_MODEL_SERIALIZATION = True
# edc.subject.consent
# set to False so that the constraint can be expanded to subject_identifier + survey
SUBJECT_IDENTIFIER_UNIQUE_ON_CONSENT = False

#  edc.device.device
DEVICE_ID = DEVICE_ID
MIDDLEMAN_DEVICE_ID_LIST = [98]
SERVER_DEVICE_ID_LIST = [91, 92, 93, 94, 95, 96, 97, 99]
if str(DEVICE_ID) == '99':
    PROJECT_TITLE = 'SERVER: Cancer Incidence and Outcomes'
elif str(DEVICE_ID) != '99':
    PROJECT_TITLE = 'TEST: Cancer Incidence and Outcomes'
