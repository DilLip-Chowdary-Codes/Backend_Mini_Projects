

REQUEST_BODY_JSON = """
{
    "name": "string",
    "description": "string",
    "workflow_id": 1,
    "project_type": "Classic Software",
    "developers": [
        1
    ]
}
"""


RESPONSE_201_JSON = """
{
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
}
"""

