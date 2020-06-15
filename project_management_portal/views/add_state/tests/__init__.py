# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "add_state"
REQUEST_METHOD = "post"
URL_SUFFIX = "states/v1/"

from .test_case_01 import TestCase01AddStateAPITestCase

__all__ = [
    "TestCase01AddStateAPITestCase"
]
