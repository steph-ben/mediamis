import platform
import settings_conf

if platform.node() == 'steph-laptopp':
    from settings_conf.local_settings import *
else:
    from settings_conf.heroku_settings import *

