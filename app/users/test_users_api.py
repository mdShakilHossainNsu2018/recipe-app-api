from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('users:create')


def create_user(**kwargs):
    return get_user_model().objects.create_user(**kwargs)


class PublicUserApi(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        payload = {
            'email': 'test@gmail.com',
            'password': '1234testpass',
            'name': 'shakil'
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEquals(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exist(self):
        payload = {
            'email': 'test@gmail.com',
            'password': '1234testpass',
        }

        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)
        
        self.assertEquals(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        payload = {
            'email': 'test1@gmail.com',
            'password': 'pw',
        }

        # create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEquals(res.status_code, status.HTTP_400_BAD_REQUEST)
        print(res.status_code)

        user = get_user_model().objects.filter(
            email=payload["email"]
        )

        user_exists = user.exists()
        self.assertFalse(user_exists)

