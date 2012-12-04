import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "mediamis",
    version = "0.1",
    license = 'All rights reserved',
    description = "Share books with your friends !",
    long_description = read('README'),
    
    author = 'Stephane Benchimol (MFI)',
    author_email = 'stephane.benchimol@mfi.fr',
    
    packages = find_packages(),
    zip_safe=False,
    install_requires = ['setuptools',
                        # Core
                        'django',
			            'psycopg2',

                        # Dev tools
                        'django-extensions',
                        'Werkzeug',
                        'django-debug-toolbar',
                        'django-autofixture',

                        # Thirds apps
                        'South',
                        'djeneralize',
                        'pil',  # For ImageField
                        'django-storages',

                        # Others apps
                        #'django-crumbs',
                        #'cx_oracle',
                        #'django-annoying',
                        #'django-autofixture',
                        #'django-olwidget',
                        #'django-piston',
                        #'django-formwizard',
                        #'django-test-utils', # ou donc ?
                        #'django-tastypie',
                        #'django-ajax-validation',

                        ],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
