"""
Create Project
"""
from freezegun import freeze_time
from project_management_portal.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "name": "Test_Project",
    "description": "Some_Random_Text",
    "workflow_id": 1,
    "project_type": "Classic Software",
    "developers": []
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {"HTTP_OAUTHTOKEN": "string"},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/v1/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}

class TestCase01CreateProjectAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01CreateProjectAPITestCase, self).setupUser(
            username, password
        )
        self.create_workflow()

    @freeze_time("2020-06-26")
    def test_case(self):
        self.default_test_case()
