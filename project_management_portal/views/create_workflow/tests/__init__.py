# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "create_workflow"
REQUEST_METHOD = "post"
URL_SUFFIX = "workflows/v1/"

from .test_case_01 import TestCase01CreateWorkflowAPITestCase

__all__ = [
    "TestCase01CreateWorkflowAPITestCase"
]
