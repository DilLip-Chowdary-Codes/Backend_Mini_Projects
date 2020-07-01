# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetProjectsAPIForNormalUserTestCase::test_case status'] = 200

snapshots['TestCase01GetProjectsAPIForNormalUserTestCase::test_case body'] = {
    'projects': [
        {
            'created_at': '2020-06-26 00:00:00',
            'created_by': 1,
            'description': 'project_1_description',
            'developers': [
                1
            ],
            'name': 'project_1',
            'project_id': 1,
            'project_type': 'Classic Software',
            'workflow': 'workflow_1'
        },
        {
            'created_at': '2020-06-26 00:00:00',
            'created_by': 1,
            'description': 'project_2_description',
            'developers': [
                1
            ],
            'name': 'project_2',
            'project_id': 2,
            'project_type': 'Financial',
            'workflow': 'workflow_1'
        },
        {
            'created_at': '2020-06-26 00:00:00',
            'created_by': 1,
            'description': 'project_3_description',
            'developers': [
                1
            ],
            'name': 'project_3',
            'project_id': 3,
            'project_type': 'CRM',
            'workflow': 'workflow_1'
        }
    ],
    'total_projects': 4
}

snapshots['TestCase01GetProjectsAPIForNormalUserTestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '660',
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
