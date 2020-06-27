# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "logout"
REQUEST_METHOD = "delete"
URL_SUFFIX = "user/logout/v1/"

from .test_case_01 import TestCase01LogoutAPITestCase
from .test_case_02 import TestCase02LogoutAPIWithInvalidTokenTestCase

__all__ = [
    "TestCase01LogoutAPITestCase",
    "TestCase02LogoutAPIWithInvalidTokenTestCase"
]
