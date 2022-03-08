from .base import *

INSTALLED_APPS = INSTALLED_APPS + ["django_extensions"]

# In DEV, we allow all origin to bypass CORS
CORS_ALLOW_ALL_ORIGINS = True