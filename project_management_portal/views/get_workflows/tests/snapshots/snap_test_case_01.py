# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetWorkflowsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetWorkflowsAPITestCase::test_case body'] = {
    'total_workflows': 5,
    'workflows': [
        {
            'name': 'workflow_1',
            'workflow_id': 1
        },
        {
            'name': 'workflow_2',
            'workflow_id': 2
        },
        {
            'name': 'workflow_3',
            'workflow_id': 3
        },
        {
            'name': 'workflow_4',
            'workflow_id': 4
        },
        {
            'name': 'workflow_5',
            'workflow_id': 5
        }
    ]
}

snapshots['TestCase01GetWorkflowsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '247',
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
