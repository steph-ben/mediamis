#!/usr/bin/env python
import sys, os, imp
from django.core.management import execute_manager

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

sys.path = [os.path.join(BASE_PATH, 'apps'),
            os.path.join(BASE_PATH, 'apps-reusable'),
            os.path.join(BASE_PATH, 'libs'),
            ] + sys.path
try:
    import settings
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
