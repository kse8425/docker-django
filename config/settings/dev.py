from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'orbis-web',
        'USER': 'orbis',
        'PASSWORD': 'fabrica',
        'HOST': '192.168.0.12',
        # 'HOST': '127.0.0.1',
        'PORT': '5000',
    }
}
