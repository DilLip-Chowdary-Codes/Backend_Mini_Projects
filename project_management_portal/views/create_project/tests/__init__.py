# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "create_project"
REQUEST_METHOD = "post"
URL_SUFFIX = "projects/v1/"

from .test_case_01 import TestCase01CreateProjectAPITestCase

__all__ = [
    "TestCase01CreateProjectAPITestCase"
]
