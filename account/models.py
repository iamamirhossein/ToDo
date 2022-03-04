from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    nick_name = models.CharField(max_length=64)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='img/profiles/', null=True)
    is_active = models.BooleanField(default=True)
