# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "get_workflows"
REQUEST_METHOD = "get"
URL_SUFFIX = "workflows/v1/"

from .test_case_01 import TestCase01GetWorkflowsAPITestCase

__all__ = [
    "TestCase01GetWorkflowsAPITestCase"
]
