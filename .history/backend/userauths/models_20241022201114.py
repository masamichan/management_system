from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  username = models.CharField(unique=True, max_length=100)
  email = models.EmailField(unique=True)
  full_name = models.CharField(unique=True, max_length=100)
  opt = models.CharField(unique=True, max_length=100)

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["username"]

  def __str__(self):
    return self.email
  
  def save(self, *arg, **kwargs):
    email_username, full_name = self.email.split("@")
    if self.full_name == "" or self.full_name == None:
      self.full_name == email_username

      

