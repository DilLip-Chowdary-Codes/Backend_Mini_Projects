# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateTaskStateAPITestCase::test_case status'] = 201

snapshots['TestCase01UpdateTaskStateAPITestCase::test_case body'] = {
    'assignee_id': 1,
    'description': 'description_1',
    'issue_type': 'Task',
    'project': 'project_1',
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
        '149',
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
