from os import environ

import dj_database_url
import os

from .settings import *

DATABASES = {
    'default': {

    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
