from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')


# 可変長の引数を用いてユーザーを作成
def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""
        payload = {
            'email': 'test@test.com',
            'password': 'test_pass',
            'name': 'Test name',
        }
        # test response_status
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        # test exact password
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))

        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Test creatings user that already exists fails"""
        payload = {
            'email': 'test@test.com',
            'password': 'test_pass',
            'name': 'Test name',
        }
        create_user(**payload)

        # test response_status
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that the password must be more than 5 characters"""
        payload = {
            'email': 'test@test.com',
            'password': 'pw',
            'name': 'Test name',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        # test response_status
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        # test not_creating_user
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)
