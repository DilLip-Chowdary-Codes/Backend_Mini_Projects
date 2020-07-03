# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestTaskStorage.test_create_task task_details_dto'] = GenericRepr('TaskDetailsDto(task_id=1, project=ProjectDto(project_id=1, name=\'projectManagement\', description="it\'s a blaw blaw blaw blaw  blaw blaw ", workflow=\'Workflow_1\', project_type=\'Classic Software\', created_by_id=1, created_at=\'2020-05-28 10:06:23\', developers_ids=[1, 2]), issue_type=\'Enhancement\', title=\'Optimizing DB\', assignee_id=1, description=\'string\', state=\'State_1\')')

snapshots['TestTaskStorage.test_get_tasks tasks_details_dtos'] = [
    GenericRepr('TaskDetailsDto(task_id=2, project=ProjectDto(project_id=1, name=\'projectManagement\', description="it\'s a blaw blaw blaw blaw  blaw blaw ", workflow=\'Workflow_1\', project_type=\'Classic Software\', created_by_id=1, created_at=\'2020-05-28 10:06:23\', developers_ids=[1, 2]), issue_type=\'BUG\', title=\'Optimizing DB\', assignee_id=2, description=\'string\', state=\'State_2\')'),
    GenericRepr('TaskDetailsDto(task_id=1, project=ProjectDto(project_id=1, name=\'projectManagement\', description="it\'s a blaw blaw blaw blaw  blaw blaw ", workflow=\'Workflow_1\', project_type=\'Classic Software\', created_by_id=1, created_at=\'2020-05-28 10:06:23\', developers_ids=[1, 2]), issue_type=\'Enhancement\', title=\'Optimizing DB\', assignee_id=1, description=\'string\', state=\'State_1\')')
]

snapshots['TestTaskStorage.test_update_task_state conditions_satisfied'] = [
    1,
    2
]

snapshots['TestTaskStorage.test_update_task_state_with_zero_satisfied_conditions conditions_satisfied'] = [
]

snapshots['TestTaskStorage.test_validate_state_id is_state_valid'] = True

snapshots['TestTaskStorage.test_validate_state_id_with_invalid_value is_state_valid'] = False

snapshots['TestTaskStorage.test_validate_task_id task_dto'] = GenericRepr("TaskDto(project_id=1, issue_type='Enhancement', title='Optimizing DB', description='string', state_id=1)")

snapshots['TestTaskStorage.test_validate_task_id_with_invalid_id task_dto'] = None

snapshots['TestTaskStorage.test_get_tasks_with_no_tasks tasks_details_dtos'] = [
]

snapshots['TestTaskStorage.test_update_task_state state'] = 'State_2'

snapshots['TestTaskStorage.test_update_task_state_with_zero_satisfied_conditions state'] = 'State_3'

snapshots['TestTaskStorage.test_get_states_for_task_based_on_current_state states_dtos'] = [
    GenericRepr("StateDetailsDto(state_id=2, name='State_2')"),
    GenericRepr("StateDetailsDto(state_id=3, name='State_3')")
]

snapshots['TestTaskStorage.test_get_states_for_task_based_on_current_state_no_states states_dtos'] = [
]
