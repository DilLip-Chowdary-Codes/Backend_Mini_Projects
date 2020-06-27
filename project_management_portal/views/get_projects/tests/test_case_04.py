"""
Get Projects With Invalid Limit
"""

from project_management_portal.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """

"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {"limit": -1, "offset": 0, "sort_by": True},
        "header_params": {"HTTP_OAUTHTOKEN": "string"},
        "securities": {
            "oauth": {
                "tokenUrl": "http://auth.ibtspl.com/oauth2/v1/",
                "flow": "password",
                "scopes": ["read", "write", "superuser"], "type": "oauth2"}
        },
        "body": REQUEST_BODY,
    },
}

class TestCase04GetProjectsAPIWithInvalidLimitTestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE
    
    def setupUser(self, username, password):
        super(TestCase04GetProjectsAPIWithInvalidLimitTestCase, self)\
            .setupUser(username, password)

    def test_case(self):
        self.default_test_case()
