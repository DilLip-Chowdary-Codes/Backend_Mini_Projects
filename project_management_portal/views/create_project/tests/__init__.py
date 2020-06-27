# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "create_project"
REQUEST_METHOD = "post"
URL_SUFFIX = "projects/v1/"

from .test_case_01 import TestCase01CreateProjectAPITestCase
from .test_case_02\
    import TestCase02CreateProjectAPITestCaseWithInvalidWorkflow
from .test_case_03 import TestCase03CreateProjectAPITestCaseWithInvalidType

__all__ = [
    "TestCase01CreateProjectAPITestCase",
    "TestCase02CreateProjectAPITestCaseWithInvalidWorkflow",
    "TestCase03CreateProjectAPITestCaseWithInvalidType"
]
