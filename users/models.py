from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    address = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to="profile/", blank=True)
    description = models.TextField(blank=True)

    