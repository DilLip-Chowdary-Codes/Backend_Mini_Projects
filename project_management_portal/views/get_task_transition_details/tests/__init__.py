# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "get_task_transition_details"
REQUEST_METHOD = "post"
URL_SUFFIX = "projects/{project_id}/tasks/{task_id}/transition/details/v1/"

from .test_case_01 import TestCase01GetTaskTransitionDetailsAPITestCase

__all__ = [
    "TestCase01GetTaskTransitionDetailsAPITestCase"
]
