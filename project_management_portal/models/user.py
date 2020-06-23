from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import ValidationError
from django import forms

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    profile_pic = models.URLField()
    phone_no = models.CharField(max_length=12)
    is_admin = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    lang = models.CharField(max_length=100)

    def __str__(self):
        return self.email
