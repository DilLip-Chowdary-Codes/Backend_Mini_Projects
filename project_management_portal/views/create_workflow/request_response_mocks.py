

REQUEST_BODY_JSON = """
{
    "type": "string",
    "states": [
        1
    ],
    "transitions": [
        1
    ]
}
"""


RESPONSE_201_JSON = """
{
    "type": "string",
    "states": [
        {
            "state": "string"
        }
    ],
    "transitions": [
        {
            "from_state": "string",
            "to_state": "string",
            "name": "string",
            "description": "string"
        }
    ]
}
"""

