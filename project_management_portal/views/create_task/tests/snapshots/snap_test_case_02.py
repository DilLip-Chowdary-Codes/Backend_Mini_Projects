# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02CreateTaskAPITestCaseWithInvalidIssueType::test_case status'] = 400

snapshots['TestCase02CreateTaskAPITestCaseWithInvalidIssueType::test_case body'] = {
    'issue_type': [
        '"BUG Report" is not a valid choice.'
    ]
}

snapshots['TestCase02CreateTaskAPITestCaseWithInvalidIssueType::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '56',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
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
