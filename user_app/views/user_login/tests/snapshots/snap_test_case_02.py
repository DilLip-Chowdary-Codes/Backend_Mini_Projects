# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UserLoginAPIForAdminTestCase::test_case status'] = 200

snapshots['TestCase02UserLoginAPIForAdminTestCase::test_case body'] = {
    'access_token': 'test_access_token',
    'expires_in': '1000000',
    'is_admin': True,
    'profile_pic': '',
    'refresh_token': 'test_refresh_token',
    'user_id': 1,
    'username': 'admin_1'
}

snapshots['TestCase02UserLoginAPIForAdminTestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '175',
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
