# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateTaskAPITestCase::test_case status'] = 201

snapshots['TestCase01CreateTaskAPITestCase::test_case body'] = {
    'assignee_id': {
        'phone_no': '9999999999',
        'profile_pic': 'http://www.google.com',
        'user_id': 1,
        'username': 'username_1'
    },
    'description': 'string',
    'issue_type': 'BUG',
    'project': {
        'created_at': '2020-06-26 00:00:00',
        'created_by': {
            'phone_no': '9999999999',
            'profile_pic': 'http://www.google.com',
            'user_id': 1,
            'username': 'username_1'
        },
        'description': 'project_1_description',
        'developers': [
            1,
            2
        ],
        'name': 'project_1',
        'project_id': 1,
        'project_type': 'Classic Software',
        'workflow': 'workflow_1'
    },
    'state': 'state_1',
    'task_id': 6,
    'title': 'string'
}

snapshots['TestCase01CreateTaskAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '556',
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
