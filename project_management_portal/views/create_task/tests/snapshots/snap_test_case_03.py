# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03CreateTaskAPITestCaseWithInvalidStateId::test_case status'] = 404

snapshots['TestCase03CreateTaskAPITestCaseWithInvalidStateId::test_case body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_STATE',
    'response': 'Invalid state_id, try with valid state_id'
}

snapshots['TestCase03CreateTaskAPITestCaseWithInvalidStateId::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '113',
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
