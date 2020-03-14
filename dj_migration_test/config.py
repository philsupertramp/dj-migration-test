import django
from django.core.signals import setting_changed
from django.conf import settings as django_settings

DEFAULTS = {
    'DJANGO_VERSION': django.get_version()
}


class SettingNotFound(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class Settings(object):
    prefix = 'MIGRATION_TEST_'

    def __init__(self):
        self.reset_settings()
        setting_changed.connect(self.set_setting)

    def __getattr__(self, item):
        split_name = item.split(self.prefix)
        if len(split_name) > 1 and split_name[1] not in DEFAULTS:
            raise SettingNotFound(f'Can\'t find setting {item}.')
        value = self.get_setting(item)
        setattr(self, item, value)
        return value

    def get_setting(self, setting):
        assert setting.startswith(self.prefix), f'Unknown setting {setting}'
        return getattr(django_settings, setting, DEFAULTS[setting.split(self.prefix)[1]])

    def set_setting(self, setting, value, enter=False, **kwargs):
        if not setting.startswith(self.prefix):
            return
        setting = setting[len(self.prefix):]

        # ensure a valid app setting is being overridden
        if setting not in DEFAULTS:
            return

        # if exiting, delete value to repopulate
        if enter:
            setattr(self, setting, value)
        else:
            delattr(self, setting)

    def reset_settings(self):
        for setting, value in DEFAULTS.items():
            setattr(self, setting, value)
