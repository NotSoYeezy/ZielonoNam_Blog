from distutils.command.upload import upload
from importlib.metadata import requires
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    profile_pic = models.ImageField(upload_to='profile_pics')

    def __str__(self) -> str:
        return self.username