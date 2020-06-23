from django.db import models
from .user import User
class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, through='GroupLevel')

class GroupLevel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    rank = models.IntegerField()

