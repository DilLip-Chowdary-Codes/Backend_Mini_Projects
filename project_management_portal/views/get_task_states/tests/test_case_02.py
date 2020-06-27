"""
Get Task States With Invalid Project_ID
"""

from project_management_portal.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """

"""

TEST_CASE = {
    "request": {
        "path_params": {
            "project_id": "2",
            "task_id": "1"
        },
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/v1/", "flow": "password", "scopes": ["read", "write"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}

class TestCase02GetTaskStatesAPIWithInvalidProjectTestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE
    
    def setupUser(self, username, password):
        super(TestCase02GetTaskStatesAPIWithInvalidProjectTestCase, self)\
            .setupUser(username, password)
        self.create_project()
        self.create_task()

    def test_case(self):
        self.default_test_case()
