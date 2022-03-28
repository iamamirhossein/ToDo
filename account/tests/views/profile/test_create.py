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
