from django.db import models
from .transition import Transition
from .checklist import Checklist
from .user import User

class New(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checkpoint = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    is_satisfied = models.BooleanField(default=False)
