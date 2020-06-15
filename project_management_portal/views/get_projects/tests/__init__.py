# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "get_projects"
REQUEST_METHOD = "get"
URL_SUFFIX = "projects/v1/"

from .test_case_01 import TestCase01GetProjectsAPITestCase

__all__ = [
    "TestCase01GetProjectsAPITestCase"
]
