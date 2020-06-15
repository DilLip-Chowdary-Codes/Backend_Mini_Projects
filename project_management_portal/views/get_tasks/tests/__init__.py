# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "get_tasks"
REQUEST_METHOD = "get"
URL_SUFFIX = "projects/{project_id}/tasks/v1/"

from .test_case_01 import TestCase01GetTasksAPITestCase

__all__ = [
    "TestCase01GetTasksAPITestCase"
]
