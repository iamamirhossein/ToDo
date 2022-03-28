from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from account.models import Profile
from django.contrib.auth.models import User


class ProfileCreateTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.super_user = User.objects.create_superuser(username='Admin',
                                                       email='admin@admin.test',
                                                       password='1234')
        cls.normal_user = User.objects.create_user(username='new_user')
        cls.client = APIClient()
        cls.url = reverse('account:profile-list')
        cls.token_url = reverse('account:token-get')

    def temporary_image(self):
        bts = BytesIO()
        img = Image.new("RGB", (100, 100))
        img.save(bts, 'jpeg')
        return SimpleUploadedFile("test.jpg", bts.getvalue())

    def test_ok(self):
        path = self.url
        self.client.force_authenticate(user=self.super_user)
        image = self.temporary_image()
        data = {
            'nick_name': 'foo',
            'avatar': image,
        }
        response = self.client.post(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('nick_name'), 'foo')
        self.assertEqual(response.data.get('avatar').split('/')[-1], image.name)

    def test_create_with_bad_image_400(self):
        path = self.url
        self.client.force_authenticate(user=self.super_user)
        data = {
            'nick_name': 'foo',
            'avatar': 'image.jpg',
        }
        response = self.client.post(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
