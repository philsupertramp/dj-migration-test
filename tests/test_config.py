from unittest import TestCase, mock

from django.test import override_settings
from django.conf import settings as django_settings

from dj_migration_test import config


class SettingsClassTestCase(TestCase):
    def setUp(self) -> None:
        self.settings = config.Settings()
    
    def test_init(self):
        """Config: Test for default settings after initialization"""
        for key in config.DEFAULTS:
            self.assertIsNotNone(getattr(self.settings, f'MIGRATION_TEST_{key}'))

    def test_reset_settings(self):
        """Config: Test reset for settings keeps user value"""
        setting_name = 'MIGRATION_TEST_DJANGO_VERSION'
        setting_value = 'ERROR'
        with override_settings(**{setting_name: setting_value}):
            self.settings.reset_settings()
            self.assertEqual(getattr(self.settings, setting_name), getattr(django_settings, setting_name))

    def test_change_settings(self):
        for key in config.DEFAULTS:
            with override_settings(**{f'MIGRATION_TEST_{key}': 'TEST'}):
                self.assertEqual(getattr(self.settings, f'MIGRATION_TEST_{key}'), 'TEST')

    @mock.patch('dj_migration_test.config.Settings.set_setting')
    def test_change_settings_ignored(self, setter):
        with override_settings(TEST=True):
            pass

        with override_settings(MIGRATION_TEST_VERBOSITY=2):
            pass

    def test_get_settings(self):
        with self.assertRaises(AssertionError):
            getattr(self.settings, 'WITHOUT_PREFIX')

        with self.assertRaises(config.SettingNotFound):
            getattr(self.settings, 'MIGRATION_TEST_WITH_PREFIX')
