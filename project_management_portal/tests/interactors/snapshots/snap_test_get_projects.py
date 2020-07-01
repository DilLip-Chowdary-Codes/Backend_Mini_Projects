# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetProjects.test_get_projects_for_admin project_details'] = [
    {
        'created_at': '2020-05-28 10:06:23',
        'created_by': {
            'phone_no': '8739835635',
            'profile_pic': 'http://www.google.com/',
            'user_id': 1,
            'username': 'username_1'
        },
        'description': "it's a blaw blaw blaw blaw  blaw blaw ",
        'developers': [
            {
                'phone_no': '8739835635',
                'profile_pic': 'http://www.google.com/',
                'user_id': 2,
                'username': 'username_2'
            }
        ],
        'name': 'projectManagement',
        'project_type': 'Classic Software',
        'workflow': ''
    }
]

snapshots['TestGetProjects.test_get_projects_for_normal_user project_details'] = [
    {
        'created_at': '2020-05-28 10:06:23',
        'created_by': {
            'phone_no': '8739835635',
            'profile_pic': 'http://www.google.com/',
            'user_id': 1,
            'username': 'username_1'
        },
        'description': "it's a blaw blaw blaw blaw  blaw blaw ",
        'developers': [
            {
                'phone_no': '8739835635',
                'profile_pic': 'http://www.google.com/',
                'user_id': 2,
                'username': 'username_2'
            }
        ],
        'name': 'projectManagement',
        'project_type': 'Classic Software',
        'workflow': ''
    }
]
