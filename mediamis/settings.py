import platform
import settings_conf

if platform.node() == 'steph-laptopp':
    import settings_conf.local_settings as settings
else:
    import settings_conf.heroku_settings as settings