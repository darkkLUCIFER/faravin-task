from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    is_creator = models.BooleanField(default=False, blank=True)
    is_viewer = models.BooleanField(default=False, blank=True)
