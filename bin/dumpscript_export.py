""" Export data to python script
    $ python mediamis/manage.py dumpscript auth.User
    $ python mediamis/manage.py dumpscript friendlib
"""
import sys, imp, os
from os.path import join, dirname, abspath

# Paths ...
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
FILEPATH = dirname(abspath(__file__))   # bin/
DJANGO_PROJECT = join(join(FILEPATH, '..'), 'mediamis')
EXPORT_DIR = join(DJANGO_PROJECT, 'scripts')

sys.path = [DJANGO_PROJECT,] + sys.path

# Load Django settings ...
imp.find_module('settings') # Assumed to be in the same directory.
from settings import settings

from django_extensions.management.commands import dumpscript


# Create new directory for current export
current_dir = join(EXPORT_DIR, 'new_unique_dir_with_date')

from django.contrib.auth.models import User
print User.objects.all()

app_labels = ['auth.User', 'friendlib.Media']
models = dumpscript.get_models(app_labels)
context = {}
print dumpscript.Script(models=models, context=context)
