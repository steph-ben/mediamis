"""
Setting file for Heroku

settings.py HAS TO BE a file (not a directory with __init__.py) because
Heroku add some stuff at the end of the file
"""

######## default_settings.py #################
import os
# Django settings for myfriendlylibrary project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = 'media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

SERVE_STATIC_FILES = True

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'j&gh_7)d1s2aahl=^!8f790o%8^7!!dp^pg17x7#ut@zxl@2nx'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "../templates"),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'registration.middleware.LoginFormMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'friendlib.middleware.MediamisContextMiddleware'
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Useful apps for dev
    'django_extensions',    # Add several commands to manage.py
    'south',                # Manage database changes easily (eg. new columns)
    'autofixture',

    # Thirds apps
    'djeneralize',

    # Reusable apps
    'registration',

    'friendlib',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}




############## heroku_settings.py #################

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



# Dev server serve /media files
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_URL = 'http://vivid-rain-4083.herokuapp.com/friendlib'
#PROJECT_URL = 'http://localhost/friendlib'

SERVE_STATIC_FILES = True
STATIC_ROOT = os.path.join(PROJECT_PATH, 'staticfiles')
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
