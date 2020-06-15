# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "create_transition"
REQUEST_METHOD = "post"
URL_SUFFIX = "projects/{project_id}/workflow/transition/v1/"

from .test_case_01 import TestCase01CreateTransitionAPITestCase

__all__ = [
    "TestCase01CreateTransitionAPITestCase"
]
