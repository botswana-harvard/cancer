TESTING_MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
        },
        'NAME': 'test_default',
        'USER': 'root',
        'PASSWORD': 'cc3721b',
        'HOST': '',
        'PORT': '',
    },
    'lab_api': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
        },
        'NAME': 'test_lab_api',
        'USER': 'root',
        'PASSWORD': 'cc3721b',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    },
    'dispatch_destination': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
        },
        'NAME': 'test_destination',
        'USER': 'root',
        'PASSWORD': 'cc3721b',
        'HOST': '',
        'PORT': '',
    },
}
