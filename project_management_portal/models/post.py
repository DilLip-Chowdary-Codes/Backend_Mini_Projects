from django.db import models
from .user import User

class Post(models.Model):

    title = models.CharField(max_length=100)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
