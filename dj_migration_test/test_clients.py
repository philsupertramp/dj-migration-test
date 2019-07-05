from django.apps import apps
from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from django.test import TransactionTestCase

from dj_migration_test.exceptions import AppNotFound


class MigrationTestCase(TransactionTestCase):
    """
    TestCase to write automated migration tests.

    To test migrations you need to add the attribute
        - migration_to: ('app_name', 'migration_name')-Tuple with the desired post-migration-state to perform tests on
        OPTIONAL
        - migration_from: List of ('app_name', 'migration_name')-Tuples containing the start state, including
        dependencies
        **you will need to add all dependencies by yourself**
    And implement the method `setUpDataBeforeMigration` which gives you the possibility to create database entries
    in state of the migration prior to `migration_to`
    """
    migrate_from = None
    migrate_to = None

    @property
    def app(self):
        return apps.get_containing_app_config(self.__module__).name.split('.')[-1]

    def _perform_migration(self, migration):
        self._executor.migrate(migration)
        return self._executor.loader.project_state(migration)

    def _get_migration_states(self):
        try:
            migrate_to = self._executor.loader.get_migration(*self.migrate_to)
        except KeyError:
            raise AppNotFound()
        if not self.migrate_from:
            migrate_from = migrate_to.dependencies
        else:
            migrate_from = self.migrate_from if isinstance(self.migrate_from, list) else [self.migrate_from]
        return migrate_from, [self.migrate_to]

    def setUp(self):
        assert self.migrate_to, \
            f'TestCase \'{type(self).__name__}\' must define migrate_to property'

        self._executor = MigrationExecutor(connection)

        migrate_from, migrate_to = self._get_migration_states()

        # revert to origin state
        old_state = self._perform_migration(migrate_from)

        # prepare data for testing based on old state
        self.setUpDataBeforeMigration(self, old_state.apps)

        # reload graph
        self._executor.loader.build_graph()

        # Run the migration to perform tests on
        self.apps = self._perform_migration(migrate_to).apps

    @staticmethod
    def setUpDataBeforeMigration(test_instance, apps):  # noqa: N802
        """Create your testing data here.
        Use :attr apps: to work with pre-migration models.

        Example:
            test_model_class = apps.get_model('test_app', 'TestModelA')

            self.thread = test_model_class.objects.create(...)
        """
        raise NotImplementedError
