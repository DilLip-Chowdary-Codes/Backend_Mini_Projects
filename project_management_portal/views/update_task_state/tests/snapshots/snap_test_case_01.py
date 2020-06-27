# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateTaskStateAPITestCase::test_case status'] = 201

snapshots['TestCase01UpdateTaskStateAPITestCase::test_case body'] = {
    'assignee': {
        'phone_no': '',
        'profile_pic': '',
        'user_id': 1,
        'username': 'username'
    },
    'description': 'description_1',
    'issue_type': 'Task',
    'project': {
        'created_at': '2020-06-26 00:00:00',
        'created_by': {
            'phone_no': '',
            'profile_pic': '',
            'user_id': 1,
            'username': 'username'
        },
        'description': 'project_1_description',
        'developers': [
            {
                'phone_no': '',
                'profile_pic': '',
                'user_id': 2,
                'username': 'user_1'
            },
            {
                'phone_no': '',
                'profile_pic': '',
                'user_id': 3,
                'username': 'user_2'
            }
        ],
        'name': 'project_1',
        'project_id': 1,
        'project_type': 'Classic Software',
        'workflow': 'workflow_1'
    },
    'state': 'state_2',
    'task_id': 1,
    'title': 'task_1'
}

snapshots['TestCase01UpdateTaskStateAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '635',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin',
        'Vary'
    ],
    'x-frame-options': [
        'DENY',
        'X-Frame-Options'
    ]
}
