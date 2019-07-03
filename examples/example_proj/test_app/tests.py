from test_clients import MigrationTestCase


class TestAppMigration0001To0003TestCase(MigrationTestCase):
    migrate_from = ('test_app', '0001_initial')
    migrate_to = ('test_app', '0003_remove_testobja_name')

    def setUpDataBeforeMigration(self, apps):
        test_obj_a_class = apps.get_model('test_app', 'TestObjA')
        test_obj_a = test_obj_a_class.objects.create(name='ab')
        self.obj_id = test_obj_a.id

    def test_name_split(self):
        test_obj_a_class = self.apps.get_model('test_app', 'TestObjA')
        test_obj_a = test_obj_a_class.objects.get(pk=self.obj_id)
        self.assertEqual(test_obj_a.first_name, 'a')
        self.assertEqual(test_obj_a.last_name, 'b')
