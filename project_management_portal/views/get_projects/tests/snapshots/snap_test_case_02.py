# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetProjectsAPIForAdminTestCase::test_case status'] = 200

snapshots['TestCase02GetProjectsAPIForAdminTestCase::test_case body'] = {
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
        },
        {
            'created_at': '2020-06-26 00:00:00',
            'created_by': 1,
            'description': 'project_4_description',
            'developers': [
                1
            ],
            'name': 'project_4',
            'project_id': 4,
            'project_type': 'Classic Software',
            'workflow': 'workflow_1'
        },
        {
            'created_at': '2020-06-26 00:00:00',
            'created_by': 1,
            'description': 'project_5_description',
            'developers': [
            ],
            'name': 'project_5',
            'project_id': 5,
            'project_type': 'Financial',
            'workflow': 'workflow_1'
        },
        {
            'created_at': '2020-06-26 00:00:00',
            'created_by': 1,
            'description': 'project_6_description',
            'developers': [
            ],
            'name': 'project_6',
            'project_id': 6,
            'project_type': 'CRM',
            'workflow': 'workflow_1'
        }
    ],
    'total_projects': 6
}

snapshots['TestCase02GetProjectsAPIForAdminTestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '1283',
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
