from dj_migration_test.test_clients import MigrationTestCase


class TestAppMigration0001To0003TestCase(MigrationTestCase):
    migrate_from = ('test_app', '0001_initial')
    migrate_to = ('test_app', '0003_remove_testobja_name')

    @staticmethod
    def setUpDataBeforeMigration(test_instance, apps):
        test_obj_a_class = apps.get_model('test_app', 'TestObjA')
        test_obj_a = test_obj_a_class.objects.create(name='ab')
        test_instance.obj_id = test_obj_a.id

    def test_name_split(self):
        test_obj_a_class = self.apps.get_model('test_app', 'TestObjA')
        test_obj_a = test_obj_a_class.objects.get(pk=self.obj_id)
        self.assertEqual(test_obj_a.first_name, 'a')
        self.assertEqual(test_obj_a.last_name, 'b')


class TestAppMigration0003To0004TestCase(MigrationTestCase):
    migrate_to = ('test_app', '0004_auto_20190727_1225')

    @staticmethod
    def setUpDataBeforeMigration(test_instance, apps):
        test_obj_a_class = apps.get_model('test_app', 'TestObjA')
        test_obj_a = test_obj_a_class.objects.create(first_name='a', last_name='b')
        test_instance.obj_id = test_obj_a.id

    def test_sth(self):
        test_obj_a_class = self.apps.get_model('test_app', 'TestObjA')
        test_obj_a = test_obj_a_class.objects.get(pk=self.obj_id)
        self.assertEqual(test_obj_a.fk_dep, None)


class TestAppMigration0003To0004_2TestCase(MigrationTestCase):
    migrate_from = ('test_app', '0003_remove_testobja_name')
    migrate_to = ('test_app', '0004_auto_20190727_1225')

    @staticmethod
    def setUpDataBeforeMigration(test_instance, apps):
        test_obj_a_class = apps.get_model('test_app', 'TestObjA')
        test_obj_a = test_obj_a_class.objects.create(first_name='a', last_name='b')
        test_instance.obj_id = test_obj_a.id

    def test_sth(self):
        test_obj_a_class = self.apps.get_model('test_app', 'TestObjA')
        test_obj_a = test_obj_a_class.objects.get(pk=self.obj_id)
        self.assertEqual(test_obj_a.fk_dep, None)


class TestAppMigration0004To0005TestCase(MigrationTestCase):
    migrate_from = ('test_app', '0003_remove_testobja_name')
    migrate_to = ('test_app', '0005_testobja_second_fk_dep')

    @staticmethod
    def setUpDataBeforeMigration(test_instance, apps):
        test_obj_a_class = apps.get_model('test_app', 'TestObjA')
        test_obj_a = test_obj_a_class.objects.create(first_name='a', last_name='b')
        test_instance.obj_id = test_obj_a.id

    def test_sth(self):
        test_obj_a_class = self.apps.get_model('test_app', 'TestObjA')
        test_obj_a = test_obj_a_class.objects.get(pk=self.obj_id)
        self.assertEqual(test_obj_a.fk_dep, None)
