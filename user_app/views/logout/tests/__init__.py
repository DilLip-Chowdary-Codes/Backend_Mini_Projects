# pylint: disable=wrong-import-position

APP_NAME = "user_app"
OPERATION_NAME = "logout"
REQUEST_METHOD = "delete"
URL_SUFFIX = "user/logout/v1/"

from .test_case_01 import TestCase01LogoutAPITestCase

__all__ = [
    "TestCase01LogoutAPITestCase"
]
