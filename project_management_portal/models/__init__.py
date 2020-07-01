from .project import Project, Developer
from .workflow import Workflow
from .transition import Transition
from .state import State
from .task import Task
from .checklist import Checklist

__all__ = ["Developer", "Project", "Workflow",
    "Transition", "State", "Task", "Checklist"]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique
#         :var value: String field which will be of 128 char length
#     """
#     key = models.CharField(max_length=128, unique=True)
#     value = models.CharField(max_length=128)
#
#     class Meta(object):
#         app_label = 'sample_app'
#
#     def __str__(self):
#         return "<DummyModel: {key}-{value}>".format(key=self.key,
#                                                     value=self.value)
#
