# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetTaskTransitionDetailsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetTaskTransitionDetailsAPITestCase::test_case body'] = {
    'check_list': [
        {
            'checklist_id': 1,
            'is_required': True,
            'name': 'check_1'
        },
        {
            'checklist_id': 2,
            'is_required': True,
            'name': 'check_2'
        },
        {
            'checklist_id': 3,
            'is_required': True,
            'name': 'check_3'
        },
        {
            'checklist_id': 4,
            'is_required': True,
            'name': 'check_4'
        },
        {
            'checklist_id': 5,
            'is_required': True,
            'name': 'check_5'
        }
    ],
    'from_state': {
        'name': 'state_1',
        'state_id': 1
    },
    'to_state': {
        'name': 'state_2',
        'state_id': 2
    }
}

snapshots['TestCase01GetTaskTransitionDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '419',
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
