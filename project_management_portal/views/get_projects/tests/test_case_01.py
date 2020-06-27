"""
Get Projects For Normal_User
"""

from project_management_portal.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {"limit": 3, "offset": 0, "sort_by": True},
        "header_params": {"HTTP_OAUTHTOKEN": "string"},
        "securities": {"oauth": {
            "tokenUrl": "http://auth.ibtspl.com/oauth2/v1/",
            "flow": "password",
            "scopes": ["read", "write", "superuser"],
            "type": "oauth2"}
        },
        "body": REQUEST_BODY,
    },
}

class TestCase01GetProjectsAPIForNormalUserTestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01GetProjectsAPIForNormalUserTestCase, self).setupUser(
                username, password)
        admin = self.create_user_admin()
        self.create_projects(user=admin)

    def test_case(self):
        self.default_test_case()
