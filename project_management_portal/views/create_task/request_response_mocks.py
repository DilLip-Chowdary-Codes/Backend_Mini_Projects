

REQUEST_BODY_JSON = """
{
    "issue_type": "TASK",
    "title": "string",
    "description": "string",
    "state_id": 1
}
"""


RESPONSE_201_JSON = """
{
    "project": {
        "project_id": 1,
        "name": "string",
        "description": "string",
        "workflow_type": "todo",
        "project_type": "Classic Software",
        "created_by": {
            "username": "string",
            "profile_pic": "string",
            "phone_no": "string"
        },
        "created_at": "string",
        "developers": [
            {
                "username": "string",
                "profile_pic": "string",
                "phone_no": "string"
            }
        ]
    },
    "issue_type": "string",
    "title": "string",
    "assigned_to": [
        {
            "username": "string",
            "profile_pic": "string",
            "phone_no": "string"
        }
    ],
    "description": "string",
    "state": "string"
}
"""

