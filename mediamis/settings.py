import platform
import settings_conf

if platform.node() == 'steph-laptop':
    import settings_conf.local_settings as settings
else:
    import settings_conf.heroku_settings as settings


import dj_database_url

if 'DATABASES' not in locals():
    DATABASES = {}

if not 'default' in DATABASES:
    DATABASES['default'] = {}

DATABASES['default'].update(dj_database_url.config(default='postgres://'))