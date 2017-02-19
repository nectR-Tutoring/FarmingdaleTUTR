from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# BDD Apps
INSTALLED_APPS += ('behave_django',)

try:
    from .local import *
except ImportError:
    pass
