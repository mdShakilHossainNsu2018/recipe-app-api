from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successfully(self):
        email = 'test@gmail.com'
        password = 'testpass'

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        # print("user.email")
        self.assertEqual(email, user.email)
        self.assertTrue(user.check_password(password))

    def test_normalize_email_field(self):
        email = 'shakil@GMAIL.com'

        user = get_user_model().objects.create_user(email=email, password='passtest')
        # print('running as')

        self.assertEqual(user.email, email.lower())

    def test_email_invalid(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'something')

    def test_create_supper_user(self):
        user = get_user_model().objects.create_superuser('shakil@gmail.com', 'simpleTest')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
