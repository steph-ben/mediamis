
import os.path
import logging
logging.basicConfig(level=logging.DEBUG)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
# See debug_toolbar/panels/sql.py
SQL_DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mediamis',                      # Or path to database file if using sqlite3.
        'USER': 'mediamis',                      # Not used with sqlite3.
        'PASSWORD': 'mediamis',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


LOCAL = True
# Dev server serve /media files
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_URL = 'http://vivid-rain-4083.herokuapp.com/friendlib'
if LOCAL:
    PROJECT_URL = 'http://localhost/friendlib'

SERVE_STATIC_FILES = True
STATIC_ROOT = os.path.join(PROJECT_PATH, 'staticfiles')
if LOCAL:
    MEDIA_ROOT = STATIC_ROOT
    STATIC_ROOT = None      # MEDIA_ROOT & STATIC_ROOT must have different values, but don't know why ...
STATIC_URL = PROJECT_URL + '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'media'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)



# For debug toolbar
#INSTALLED_APPS += ('debug_toolbar',)
#INTERNAL_IPS = ('127.0.0.1',)
#MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
#DEBUG_TOOLBAR_CONFIG = {
#    'INTERCEPT_REDIRECTS': False,
#    'HIDE_DJANGO_SQL': True,
#}
