# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "get_users"
REQUEST_METHOD = "get"
URL_SUFFIX = "users/v1/"

from .test_case_01 import TestCase01GetUsersAPITestCase

__all__ = [
    "TestCase01GetUsersAPITestCase"
]
