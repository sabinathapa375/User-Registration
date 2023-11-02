from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=255,blank=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

     
