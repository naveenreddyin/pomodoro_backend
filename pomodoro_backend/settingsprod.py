from os import environ

import dj_database_url
import os

from .settings import *

DATABASES = {
    'default': {

    }
}

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


# for static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
