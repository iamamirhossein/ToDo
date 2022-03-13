from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from account.models import Profile
from django.contrib.auth.models import User


class ProfileTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.super_user = User.objects.create_superuser(username='Admin',
                                                       email='admin@admin.test',
                                                       password='1234')
        cls.normal_user = User.objects.create_user(username='new_user')
        Profile.objects.create(
            nick_name='superuser',
            user=cls.super_user
        )
        cls.client = APIClient()
        cls.url = reverse('account:profile-list')
        cls.token_url = reverse('account:token-get')

    def get_token(self):
        response = self.client.post(self.token_url, data={
            'username': self.super_user.username,
            'password': "1234"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data.get('access', '')

    def test_ok(self):
        path = self.url
        self.client.force_authenticate(user=self.super_user)
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized(self):
        path = self.url
        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
