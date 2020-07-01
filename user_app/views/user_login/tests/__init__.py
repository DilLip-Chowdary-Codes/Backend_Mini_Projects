# pylint: disable=wrong-import-position

APP_NAME = "user_app"
OPERATION_NAME = "user_login"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/login/v1/"

from .test_case_01 import TestCase01UserLoginAPITestCase
from .test_case_02 import TestCase02UserLoginAPIForAdminTestCase
from .test_case_03 import TestCase03UserLoginAPIWithInvalidUserTestCase
from .test_case_04 import TestCase04UserLoginAPIWithInvlaidPasswdTestCase

__all__ = [
    "TestCase01UserLoginAPITestCase",
    "TestCase02UserLoginAPIForAdminTestCase",
    "TestCase03UserLoginAPIWithInvalidUserTestCase",
    "TestCase04UserLoginAPIWithInvlaidPasswdTestCase"
]
