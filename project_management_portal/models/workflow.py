from django.db import models
from .state import State
from .user import User
from .transition import Transition

class Workflow(models.Model):
    name = models.CharField(max_length=100)
    states = models.ManyToManyField(State)
    transitions = models.ManyToManyField(Transition)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
