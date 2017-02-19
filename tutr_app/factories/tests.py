# BDD Factories testing file
from django.test import TestCase
from passlib.hash import django_pbkdf2_sha256

from tutr_app.factories.user import User


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
        password = 'password'
        user = User(password=password)

        self.assertIsNot(user.password, 'password')
        assert (django_pbkdf2_sha256.verify(password, user.password))
