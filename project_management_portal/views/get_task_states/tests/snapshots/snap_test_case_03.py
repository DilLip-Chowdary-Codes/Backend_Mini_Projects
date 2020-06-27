# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03GetTaskStatesAPIWithInvalidTaskTestCase::test_case status'] = 200

snapshots['TestCase03GetTaskStatesAPIWithInvalidTaskTestCase::test_case body'] = {
    'states': [
        {
            'name': 'state_2',
            'state_id': 2
        }
    ],
    'total_states': 1
}

snapshots['TestCase03GetTaskStatesAPIWithInvalidTaskTestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '67',
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
