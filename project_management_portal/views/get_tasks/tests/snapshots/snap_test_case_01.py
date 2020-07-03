# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetTasksAPITestCase::test_case status'] = 200

snapshots['TestCase01GetTasksAPITestCase::test_case body'] = {
    'project': 'project_1',
    'tasks': [
        {
            'assignee_id': 1,
            'description': 'description_1',
            'issue_type': 'Task',
            'state': 'state_1',
            'task_id': 1,
            'title': 'task_1'
        },
        {
            'assignee_id': 1,
            'description': 'description_2',
            'issue_type': 'Bug',
            'state': 'state_1',
            'task_id': 2,
            'title': 'task_2'
        },
        {
            'assignee_id': 1,
            'description': 'description_3',
            'issue_type': 'Developer Story',
            'state': 'state_1',
            'task_id': 3,
            'title': 'task_3'
        },
        {
            'assignee_id': 1,
            'description': 'description_4',
            'issue_type': 'User Story',
            'state': 'state_1',
            'task_id': 4,
            'title': 'task_4'
        },
        {
            'assignee_id': 1,
            'description': 'description_5',
            'issue_type': 'Enhancement',
            'state': 'state_1',
            'task_id': 5,
            'title': 'task_5'
        }
    ],
    'total_tasks': 5
}

snapshots['TestCase01GetTasksAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '711',
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
