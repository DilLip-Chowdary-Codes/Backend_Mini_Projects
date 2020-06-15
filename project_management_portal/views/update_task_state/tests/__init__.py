# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "update_task_state"
REQUEST_METHOD = "put"
URL_SUFFIX = "projects/{project_id}/tasks/{task_id}/state/update/v1/"

from .test_case_01 import TestCase01UpdateTaskStateAPITestCase

__all__ = [
    "TestCase01UpdateTaskStateAPITestCase"
]
