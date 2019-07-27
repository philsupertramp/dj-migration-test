import os
from unittest import TestCase

import django
from django.db import connection
from django.test.utils import teardown_databases

from dj_migration_test.exceptions import AppNotFound
from dj_migration_test.test_clients import MigrationTestCase

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings.test_settings'
django.setup()


def setUpDataBeforeMigration(test_instance, apps):
    test_obj_a_class = apps.get_model('tests', 'TestObjA')
    test_obj_a = test_obj_a_class.objects.create(name='ab')
    test_instance.obj_id = test_obj_a.id


class DjangoTestCase(TestCase):
    @classmethod
    def tearDownClass(cls) -> None:
        teardown_databases([(connection, 'default', True)], verbosity=0)


class ConfigurationTestCase(DjangoTestCase):
    def setUp(self) -> None:
        self.test_case = MigrationTestCase()

    def __reset_test_case(self):
        # tweak to reset database
        self.tearDownClass()
        self.test_case = MigrationTestCase()

    def test_missing_migrate_to(self):
        with self.assertRaises(AssertionError):
            self.test_case.setUp()

    def test_wrong_app_in_migrate_attrs(self):
        self.test_case.migrate_from = ('test_app', '0001_initial')
        self.test_case.migrate_to = ('test_app', '0003_remove_testobja_name')
        with self.assertRaises(AppNotFound):
            self.test_case.setUp()

    def test_missing_setUpDataBeforeMigration(self):
        self.test_case.migrate_from = ('tests', '0001_initial')
        self.test_case.migrate_to = ('tests', '0003_remove_testobja_name')
        with self.assertRaises(NotImplementedError):
            self.test_case.setUp()

    def test_right_complete_config(self):
        self.test_case.migrate_from = ('tests', '0001_initial')
        self.test_case.migrate_to = ('tests', '0003_remove_testobja_name')
        self.test_case.setUpDataBeforeMigration = setUpDataBeforeMigration
        self.test_case.setUp()

        self.__reset_test_case()

    def test_right_config(self):
        self.test_case.migrate_to = ('tests', '0003_remove_testobja_name')
        self.test_case.setUpDataBeforeMigration = setUpDataBeforeMigration
        self.test_case.setUp()

        self.__reset_test_case()


class PropertyTestCase(DjangoTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_case = MigrationTestCase()
        cls.test_case.migrate_from = ('tests', '0001_initial')
        cls.test_case.migrate_to = ('tests', '0003_remove_testobja_name')
        cls.test_case.setUpDataBeforeMigration = setUpDataBeforeMigration


class FirstPropertyTestCase(PropertyTestCase):
    def test_apps_attribute(self):
        self.test_case.setUp()
        apps = self.test_case.apps

        self.assertTrue(apps.is_installed('tests'))
        self.assertIn('tests', apps.all_models)


class SecondPropertyTestCase(PropertyTestCase):
    def test_app_property(self):
        self.test_case.setUp()
        app = self.test_case.app

        self.assertEqual(app, None)


class MigrationNotImplementedSetupStep(DjangoTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_case = MigrationTestCase()
        cls.test_case.migrate_to = ('tests', '0003_remove_testobja_name')

    def test_exception(self):
        with self.assertRaises(NotImplementedError):
            self.test_case.setUp()


class MigrationExecutionTestCase(DjangoTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_case = MigrationTestCase()
        cls.test_case.migrate_to = ('tests', '0003_remove_testobja_name')
        cls.test_case.setUpDataBeforeMigration = setUpDataBeforeMigration
        cls.test_case.setUp()

    def test_get_migration_states(self):
        migrate_from, migrate_to = self.test_case._get_migration_states()
        self.assertEqual(migrate_from, [('tests', '0002_auto_20190703_1731')])
        self.assertEqual(migrate_to, [('tests', '0003_remove_testobja_name')])

        self.test_case.migrate_from = ('tests', '0001_initial')

        migrate_from, migrate_to = self.test_case._get_migration_states()
        self.assertEqual(migrate_from, [('tests', '0001_initial')])
        self.assertEqual(migrate_to, [('tests', '0003_remove_testobja_name')])

    def test_perform_migration(self):
        migrate_from, migrate_to = self.test_case._get_migration_states()

        # backward
        self.test_case._perform_migration(migrate_from)

        # forward
        self.test_case._perform_migration(migrate_to)

        # explicit
        self.test_case._perform_migration([('tests', '0002_auto_20190703_1731')])
