from django.db import models
from .state import State
from .checklist import Checklist

class Transition(models.Model):
    name = models.CharField(max_length=100)
    from_state = models.ForeignKey(State,
                                   on_delete=models.CASCADE,
                                   related_name='from_state')
    to_state = models.ForeignKey(State,
                                 on_delete=models.CASCADE,
                                 related_name='to_state')
    checklist = models.ManyToManyField(Checklist)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.from_state}-->{self.to_state}"
