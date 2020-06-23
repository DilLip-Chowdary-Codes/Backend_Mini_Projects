from django.db import models
from .user import User

class Country(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=100)

class Company(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country,  on_delete=models.CASCADE)
