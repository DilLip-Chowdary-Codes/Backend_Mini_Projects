from django.db import models
from .project import Project
from .user import User
from .state import State
from .checklist import Checklist
from project_management_portal.constants.enums import IssueType

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    issue_type = models.CharField(
        max_length=100,
        choices=IssueType.get_list_of_tuples())
    title = models.CharField(max_length=100)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    conditions_satisfied = models.ManyToManyField(Checklist)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
