# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "get_projects"
REQUEST_METHOD = "get"
URL_SUFFIX = "projects/v1/"

from .test_case_01 import TestCase01GetProjectsAPIForNormalUserTestCase
from .test_case_02 import TestCase02GetProjectsAPIForAdminTestCase
from .test_case_03 import TestCase03GetProjectsAPIWithInvalidLimitTestCase
from .test_case_04 import TestCase04GetProjectsAPIWithInvalidLimitTestCase
from .test_case_05\
    import TestCase05GetProjectsAPIWithInvalidOffsetTestCase
from .test_case_06\
    import TestCase06GetProjectsAPIWithInvalidLimitTestCase

__all__ = [
    "TestCase01GetProjectsAPIForNormalUserTestCase",
    "TestCase02GetProjectsAPIForAdminTestCase",
    "TestCase03GetProjectsAPIWithInvalidLimitTestCase",
    "TestCase04GetProjectsAPIWithInvalidLimitTestCase",
    "TestCase05GetProjectsAPIWithInvalidOffsetTestCase",
    "TestCase06GetProjectsAPIWithInvalidLimitTestCase"
]
