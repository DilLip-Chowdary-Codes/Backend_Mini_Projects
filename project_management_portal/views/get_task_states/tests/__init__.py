# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "get_task_states"
REQUEST_METHOD = "get"
URL_SUFFIX = "projects/{project_id}/tasks/{task_id}/states/v1/"

from .test_case_01 import TestCase01GetTaskStatesAPITestCase
from .test_case_02 import TestCase02GetTaskStatesAPIWithInvalidProjectTestCase
from .test_case_03 import TestCase03GetTaskStatesAPIWithInvalidTaskTestCase

__all__ = [
    "TestCase01GetTaskStatesAPITestCase",
    "TestCase02GetTaskStatesAPIWithInvalidProjectTestCase",
    "TestCase03GetTaskStatesAPIWithInvalidTaskTestCase"
]
