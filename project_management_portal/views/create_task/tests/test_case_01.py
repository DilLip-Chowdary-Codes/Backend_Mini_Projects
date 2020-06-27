"""
Create Task
"""

from project_management_portal.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "issue_type": "BUG",
    "title": "string",
    "assigned_to": "string",
    "description": "string",
    "state_id": 1
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"project_id": "1"},
        "query_params": {},
        "header_params": {"HTTP_OAUTHTOKEN": "string"},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/v1/", "flow": "password", "scopes": ["read", "write", "superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01CreateTaskAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE
    
    def setupUser(self, username, password):
        super(TestCase01CreateTaskAPITestCase, self).setupUser(
            username, password)
        self.create_project()

    def test_case(self):
        self.default_test_case()
