# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestProjectPresenter.test_raise_invalid_workflow_id_exception error_message'] = 'Invalid workflow, try with valid workflow'

snapshots['TestProjectPresenter.test_raise_invalid_project_id_exception error_message'] = 'Invalid project_id, try with valid project_id'

snapshots['TestProjectPresenter.test_raise_invalid_transition_exception error_message'] = 'Invalid Transition, try with valid transition'

snapshots['TestProjectPresenter.test_raise_unauthorized_developer_exception error_message'] = 'Developer not allowed to access this resource'

snapshots['TestProjectPresenter.test_raise_invalid_limit_value_exception error_message'] = 'Invalid limit value in query , try with valid values'

snapshots['TestProjectPresenter.test_raise_invalid_offset_value_exception error_message'] = 'Invalid offset value in query , try with valid values'

snapshots['TestProjectPresenter.test_get_project_details_response project_details'] = {
    'created_at': '2020-05-28 10:06:23 AM',
    'created_by': {
        'phone_no': '8739835635',
        'profile_pic': 'http://www.google.com',
        'user_id': 1,
        'username': 'username_1'
    },
    'description': "it's a blaw blaw blaw blaw  blaw blaw ",
    'developers': [
        {
            'phone_no': '8739835635',
            'profile_pic': 'http://www.google.com',
            'user_id': 1,
            'username': 'username_1'
        },
        {
            'phone_no': '8739835635',
            'profile_pic': 'http://www.google.com',
            'user_id': 2,
            'username': 'username_2'
        }
    ],
    'name': 'projectManagement',
    'project_id': 1,
    'project_type': 'Classic Software',
    'workflow': 'Workflow_1'
}

snapshots['TestProjectPresenter.test_get_projects_response projects_details'] = {
    'projects': [
        {
            'created_at': '2020-05-28 10:06:23 AM',
            'created_by': {
                'phone_no': '8739835635',
                'profile_pic': 'http://www.google.com',
                'user_id': 1,
                'username': 'username_1'
            },
            'description': "it's a blaw blaw blaw blaw  blaw blaw ",
            'developers': [
                {
                    'phone_no': '8739835635',
                    'profile_pic': 'http://www.google.com',
                    'user_id': 1,
                    'username': 'username_1'
                },
                {
                    'phone_no': '8739835635',
                    'profile_pic': 'http://www.google.com',
                    'user_id': 2,
                    'username': 'username_2'
                }
            ],
            'name': 'projectManagement',
            'project_id': 1,
            'project_type': 'Classic Software',
            'workflow': 'Workflow_1'
        },
        {
            'created_at': '2020-05-28 10:06:23 AM',
            'created_by': {
                'phone_no': '8739835635',
                'profile_pic': 'http://www.google.com',
                'user_id': 1,
                'username': 'username_1'
            },
            'description': "it's a blaw blaw blaw blaw  blaw blaw ",
            'developers': [
                {
                    'phone_no': '8739835635',
                    'profile_pic': 'http://www.google.com',
                    'user_id': 2,
                    'username': 'username_2'
                }
            ],
            'name': 'projectManagement_2',
            'project_id': 2,
            'project_type': 'Classic Software',
            'workflow': 'Workflow_2'
        }
    ],
    'total_projects': 1
}
