from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  username = models.CharField(unique=True, max_length=100)
  email = models.EmailField(unique=True)
  full_name = models.CharField(unique=True, max_length=100)
  opt = models.CharField(unique=True, max_length=100)


