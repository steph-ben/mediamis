from default_settings import *

import logging
logging.basicConfig(level=logging.DEBUG)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
# See debug_toolbar/panels/sql.py
SQL_DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '../data/friendlib.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# Dev server serve /media files
SERVE_STATIC_FILES = True


# For debug toolbar
INSTALLED_APPS += ('debug_toolbar',)
INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'HIDE_DJANGO_SQL': True,
}