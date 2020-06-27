# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UserLoginAPITestCase::test_case status'] = 200

snapshots['TestCase01UserLoginAPITestCase::test_case body'] = {
    'access_token': 'KhzVJOfIQCXSlLtamQrTxDnYCp3KGV',
    'expires_in': '2052-03-05 13:18:09.249353',
    'is_admin': False,
    'profile_pic': '',
    'refresh_token': 'aC8LhkT8UH8LR2psdGzayXpqY2TDLT',
    'user_id': 1,
    'username': 'user_1'
}

snapshots['TestCase01UserLoginAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '219',
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
