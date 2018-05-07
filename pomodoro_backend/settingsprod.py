from os import environ

import dj_database_url
import os

from .settings import *

DATABASES = {
    'default': {

    }
}

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
