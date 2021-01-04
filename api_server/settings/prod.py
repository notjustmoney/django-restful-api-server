from .base import *

MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASS = os.environ.get('MYSQL_PASS')

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
	'HOST': 'localhost',
	'PORT': '3306',
    }
}
