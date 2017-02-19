from bdd.factories.user import AdminFactory
from django.test import TestCase


# '{0}.{1}@tutrapp.com'.format(a.first_name, a.last_name).lower()

class AdminFactoryTest(TestCase):
    def setUp(self):
        # Create a Admin User from Factory
        self.factory = AdminFactory()

    def test_create_user(self):
        """
        Tests that a default admin user is created
        """
        a = AdminFactory.build(first_name='Administrator', last_name='Testing')
        assert (a.username == 'administrator.testing')
        assert (a.email == 'administrator.testing@tutrapp.com')
