# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestTaskPresenterImplementation.test_raise_invalid_task_id_exception error_message'] = 'Invalid Task, try with valid task'

snapshots['TestTaskPresenterImplementation.test_get_task_states_response task_states'] = {
    'states': [
        {
            'name': 'State_1',
            'state_id': 1
        },
        {
            'name': 'State_2',
            'state_id': 2
        }
    ],
    'total_states': 2
}

snapshots['TestTaskPresenterImplementation.test_get_task_states_response_with_no_states task_states'] = {
    'states': [
    ],
    'total_states': 0
}

snapshots['TestTaskPresenterImplementation.test_raise_invalid_state_id_exception error_message'] = 'Invalid state_id, try with valid state_id'

snapshots['TestTaskPresenterImplementation.test_get_create_task_response task_details'] = {
    'assignee_id': 1,
    'description': 'string',
    'issue_type': 'Enhancement',
    'project': 'projectManagement',
    'state': 'In Progress',
    'task_id': 1,
    'title': 'Optimizing DB'
}

snapshots['TestTaskPresenterImplementation.test_get_tasks_response tasks_details'] = {
    'project': 'projectManagement',
    'tasks': [
        {
            'assignee_id': 1,
            'description': 'string',
            'issue_type': 'Enhancement',
            'state': 'In Progress',
            'task_id': 1,
            'title': 'Optimizing DB'
        }
    ],
    'total_tasks': 1
}
