

REQUEST_BODY_JSON = """
{
    "to_state_id": 1
}
"""


RESPONSE_200_JSON = """
{
    "task_id": 1,
    "from_state": {
        "state_id": 1,
        "name": "string"
    },
    "to_state": {
        "state_id": 1,
        "name": "string"
    },
    "checklist": [
        {
            "checklist_id": 1,
            "name": "string",
            "is_required": true
        }
    ]
}
"""

