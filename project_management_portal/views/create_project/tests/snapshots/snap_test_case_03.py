# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03CreateProjectAPITestCaseWithInvalidType::test_case status'] = 400

snapshots['TestCase03CreateProjectAPITestCaseWithInvalidType::test_case body'] = {
    'project_type': [
        '"Classic Softwaressssss" is not a valid choice.'
    ]
}

snapshots['TestCase03CreateProjectAPITestCaseWithInvalidType::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '70',
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
