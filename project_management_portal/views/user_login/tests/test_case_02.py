"""
User_login (Admin)
"""
from project_management_portal.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "username": "admin_1",
    "password": "password"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/v1/", "flow": "password", "scopes": [], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}

class TestCase02UserLoginAPIForAdminTestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def test_case(self):
        self.create_user_admin()
        self.default_test_case()
