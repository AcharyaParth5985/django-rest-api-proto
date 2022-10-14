from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
