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
        'NAME': 'data/friendlib.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# Dev server serve /media files
INSTALLED_APPS += ('django.contrib.staticfiles',)
SERVE_STATIC_FILES = True
#MEDIA_ROOT = "C:\Users\steph\Docs perso\Code\dev\perso\mediamis\mediamis\media"
STATIC_ROOT = "C:\Users\steph\Docs perso\Code\dev\perso\mediamis\mediamis\media"


# For debug toolbar
INSTALLED_APPS += ('debug_toolbar',)
INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'HIDE_DJANGO_SQL': True,
}

# In in default_settings now
#MIDDLEWARE_CLASSES += ('friendlib.middleware.MediamisContextMiddleware',)

## Dev server serve /media files
#PROJECT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
#PROJECT_URL = 'http://127.0.0.1/friendlib'
#
#SERVE_STATIC_FILES = True
#STATIC_ROOT = os.path.join(PROJECT_PATH, 'staticfiles')
#STATIC_URL = PROJECT_URL + '/media/'
#ADMIN_MEDIA_PREFIX = PROJECT_URL + '/admin/'
#STATICFILES_DIRS = (
#    os.path.join(PROJECT_PATH, 'media'),
#)
#STATICFILES_FINDERS = (
#    'django.contrib.staticfiles.finders.FileSystemFinder',
#    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
##    'django.contrib.staticfiles.finders.DefaultStorageFinder',
#)
#TEMPLATE_DIRS = (
#    os.path.join(PROJECT_PATH, 'templates'),
#)