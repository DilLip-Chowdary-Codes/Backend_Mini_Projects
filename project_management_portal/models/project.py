from django.db import models
from .state import State
from .transition import Transition
from .workflow import Workflow

from project_management_portal.constants.enums import Project_Type

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    project_type = models.CharField(
        max_length=100,
        choices=Project_Type.get_list_of_tuples()
        )
    created_by_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Developer(models.Model):

    user_id = models.IntegerField()
    project_id = models.IntegerField()
