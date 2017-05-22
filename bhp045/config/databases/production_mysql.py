import os
from unipath import Path

PATH = Path(os.path.dirname(os.path.realpath(__file__))).ancestor(1).child('etc')

PRODUCTION_MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(PATH, 'default.cnf'),
        },
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    },
    'lab_api': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(PATH, 'lab_api.cnf'),
        },
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    },
}
