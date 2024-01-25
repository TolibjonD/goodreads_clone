from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(default='users/default_profile_picture.jpg', upload_to='users/')