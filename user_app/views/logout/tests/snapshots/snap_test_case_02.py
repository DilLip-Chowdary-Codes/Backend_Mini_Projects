# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02LogoutAPIWithInvalidTokenTestCase::test_case status'] = 200

snapshots['TestCase02LogoutAPIWithInvalidTokenTestCase::test_case body'] = {
    'status': 'Logged out Succesfully'
}

snapshots['TestCase02LogoutAPIWithInvalidTokenTestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '36',
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
