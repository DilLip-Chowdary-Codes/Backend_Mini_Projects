"""
Create Task
"""

from user_app.dtos import UserDto
from project_management_portal.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from project_management_portal.adapters.user_service import UserService
from unittest.mock import patch

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

    @patch.object(UserService, 'interface')
    def test_case(self, interface_mock):

        user_dto = UserDto(
        user_id=1,
        username="username_1",
        is_admin=False,
        profile_pic="http://www.google.com",
        phone_no="9999999999"
        )
        interface_mock.get_user_dto.return_value = user_dto

        self.default_test_case()
