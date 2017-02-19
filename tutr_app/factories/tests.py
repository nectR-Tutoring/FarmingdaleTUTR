# BDD Factories testing file
from tutr_app.factories.user import User
from django.test import TestCase


class TestUserFactory(TestCase):
    def setUp(self):
        pass

    def test_create_user(self):
        user = User(first_name='Test', last_name='Admin')

        self.assertEqual(user.first_name, 'Test')
        self.assertEquals(user.last_name, 'Admin')

    def test_create_user_with_fake_data(self):
        user = User()

        self.assertIsNotNone(user.first_name, user.first_name)
        self.assertIsNotNone(user.last_name, user.last_name)

    def test_create_user_with_username(self):
        user = User()

        self.assertIsNotNone(user.username)

    def test_create_user_with_email(self):
        user = User()

        self.assertIsNotNone(user.email)

    def test_create_user_with_password(self):
        user = User(password='password')

        self.assertEquals(user.password, 'password')
