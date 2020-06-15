# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "create_task"
REQUEST_METHOD = "post"
URL_SUFFIX = "projects/{project_id}/tasks/v1/"

from .test_case_01 import TestCase01CreateTaskAPITestCase

__all__ = [
    "TestCase01CreateTaskAPITestCase"
]
