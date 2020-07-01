"""
User_login (Admin)
"""
from unittest.mock import patch
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from user_app.utils.custom_test_utils import CustomTestUtils
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
        with patch.object(OAuthUserAuthTokensService,
                  'create_user_auth_tokens',
                  return_value=self.user_auth_token_dto()):
            self.default_test_case()
