# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateProjectAPITestCase::test_case status'] = 201

snapshots['TestCase01CreateProjectAPITestCase::test_case body'] = {
    'created_at': '2020-06-26 00:00:00',
    'created_by': {
        'phone_no': '',
        'profile_pic': '',
        'user_id': 1,
        'username': 'username'
    },
    'description': 'Some_Random_Text',
    'developers': [
        {
            'phone_no': '',
            'profile_pic': '',
            'user_id': 1,
            'username': 'username'
        }
    ],
    'name': 'Test_Project',
    'project_id': 1,
    'project_type': 'Classic Software',
    'success_message': 'Project Created Succesfully',
    'workflow': 'workflow_1'
}

snapshots['TestCase01CreateProjectAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '405',
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
