"""
Django settings for cancer project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import configparser
import os
import sys

from django.core.management.color import color_style


style = color_style()

APP_NAME = 'cancer'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ETC_DIR = '/etc'
# ETC_DIR = os.path.join(str(PurePath(BASE_DIR).parent), 'etc')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

CONFIG_FILE = f'{APP_NAME}.conf'
CONFIG_PATH = os.path.join(ETC_DIR, APP_NAME, CONFIG_FILE)

sys.stdout.write(style.SUCCESS(f'Reading config from {CONFIG_PATH}\n'))

config = configparser.RawConfigParser()
config.read(os.path.join(CONFIG_PATH))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['django'].get('secret_key', 'blah$blah$blah')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['cancer-test.bhp.org.bw', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'tz_detect',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'django_crypto_fields.apps.AppConfig',
    'django_revision.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    #     'edc_lab_dashboard.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'edc_base_test.apps.AppConfig',
    'edc_reference.apps.AppConfig',
    'cancer.apps.AppConfig',
    'cancer.apps.EdcBaseAppConfig',
    'cancer_dashboard.apps.AppConfig',
    'cancer.apps.EdcLabelAppConfig',
    'cancer.apps.EdcMetadataAppConfig',
    'cancer.apps.EdcIdentifierAppConfig',
    'cancer.apps.EdcProtocolAppConfig',
    'cancer.apps.EdcTimepointAppConfig',
    'cancer.apps.EdcAppointmentAppConfig',
    'cancer.apps.EdcVisitTrackingAppConfig',
    'cancer.apps.CancerSubjectAppConfig',
    'cancer.apps.EdcSyncAppConfig',
    'cancer.apps.EdcSyncFilesAppConfig',
    'edc_subject_dashboard.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'cancer_visit_schedule.apps.AppConfig',
    'edc_facility.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cancer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = f'{APP_NAME}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'OPTIONS': {
#             'read_default_file': os.path.join(ETC_DIR, f'{APP_NAME}', 'mysql.conf'),
#         },
#     },
# }


if 'test' in sys.argv and 'mysql' not in DATABASES.get('default').get('ENGINE'):
    MIGRATION_MODULES = {
        "django_crypto_fields": None,
        "edc_call_manager": None,
        "edc_appointment": None,
        "edc_call_manager": None,
        "edc_consent": None,
        "edc_death_report": None,
        "edc_export": None,
        "edc_identifier": None,
        "edc_lab": None,
        "edc_metadata": None,
        "edc_rule_groups": None,
        "edc_registration": None,
        "edc_sync_files": None,
        "edc_sync": None,
        "cancer_subject": None}

if 'test' in sys.argv:
    PASSWORD_HASHERS = ('django_plainpasswordhasher.PlainPasswordHasher', )
    DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('tn', 'Setswana'),
    ('en', 'English'))


TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = config['django'].get(
    'static_root', os.path.join(BASE_DIR, APP_NAME, 'static'))
STATIC_URL = '/static/'

MEDIA_ROOT = config['django'].get(
    'media_root', os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'


KEY_PATH = config['django_crypto_fields'].get('key_path')
GIT_DIR = BASE_DIR
DEVICE_ID = config['edc_device'].get('device_id', '99')
DEVICE_ROLE = config['edc_device'].get('role', 'CentralServer')
LABEL_PRINTER = config['edc_label'].get('label_printer', 'label_printer')

EDC_LAB_REQUISITION_MODEL = 'cancer_subject.subjectrequisition'
CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
    'PAGE_SIZE': 1,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.LimitOffsetPagination',
    )
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'

COUNTRY = 'botswana'
HOLIDAY_FILE = os.path.join(BASE_DIR, APP_NAME, 'holidays.csv')
