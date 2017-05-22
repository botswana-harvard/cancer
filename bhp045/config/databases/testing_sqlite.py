# import os

TESTING_SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'default',
        # 'NAME': os.path.join(os.path.dirname(__file__), 'test_default.db'),
        # 'TEST_NAME': os.path.join(os.path.dirname(__file__), 'test_default.db'),
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True},
    'lab_api': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'lab',
        #  'NAME': os.path.join(os.path.dirname(__file__), 'test_lab_api.db'),
        #  'TEST_NAME': os.path.join(os.path.dirname(__file__), 'test_lab_api.db'),
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True},
    'destination': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'macair',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True},
    'dispatch_destination': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'producer',
        'USER': 'root',
        'PASSWORD': 'cc3721b',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True},
}
