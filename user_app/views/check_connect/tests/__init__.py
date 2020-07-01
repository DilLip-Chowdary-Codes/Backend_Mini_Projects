# pylint: disable=wrong-import-position

APP_NAME = "user_app"
OPERATION_NAME = "check_connect"
REQUEST_METHOD = "get"
URL_SUFFIX = "check/v1/"

from .test_case_01 import TestCase01CheckConnectAPITestCase

__all__ = [
    "TestCase01CheckConnectAPITestCase"
]
