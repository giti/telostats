from __future__ import absolute_import
from .base import *

# Store files on S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Grab database info
DATABASES = {
    'default': dj_database_url.config()
}
