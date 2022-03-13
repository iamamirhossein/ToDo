from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from account.models import Profile
from django.contrib.auth.models import User


class ProfileUpdateTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.super_user = User.objects.create_superuser(username='Admin',
                                                       email='admin@admin.test',
                                                       password='1234')
        cls.normal_user = User.objects.create_user(username='new_user')
        cls.profile = Profile.objects.create(
            nick_name='superuser',
            user=cls.super_user
        )
        cls.client = APIClient()
        cls.url = reverse('account:profile-detail', kwargs={'pk': cls.profile.pk})
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
        access_token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        data = {
            'nick_name': 'foo',
        }
        response = self.client.put(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('nick_name'), 'foo')

    def test_unauthorized(self):
        path = self.url
        response = self.client.put(path)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_bad_request(self):
        path = self.url
        self.client.force_authenticate(user=self.super_user)
        response = self.client.put(path)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
