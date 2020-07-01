# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestProjectStorage.test_validate_workflow_id_with_valid_id is_workflow_valid'] = True

snapshots['TestProjectStorage.test_validate_workflow_id_with_invalid_id is_workflow_valid'] = False

snapshots['TestProjectStorage.test_validate_developer_for_project_with_valid_id is_developer_valid'] = True

snapshots['TestProjectStorage.test_validate_developer_for_project_with_valid_admin_id is_developer_valid'] = True

snapshots['TestProjectStorage.test_validate_developer_for_project_with_invalid_id is_developer_valid'] = False

snapshots['TestProjectStorage.test_create_project project_details_dto'] = GenericRepr('ProjectDetailsDto(project_id=1, name=\'projectManagement\', description="it\'s a blaw blaw blaw blaw  blaw blaw ", workflow=\'Workflow_1\', project_type=\'Classic Software\', created_by=UserDto(user_id=1, username=\'username_1\', profile_pic=\'http://www.google.com\', phone_no=\'9999999999\', is_admin=True), created_at=\'2020-05-28 10:06:23\', developer_ids=[1])')

snapshots['TestProjectStorage.test_create_project_with_no_developers project_details_dto'] = GenericRepr('ProjectDetailsDto(project_id=1, name=\'projectManagement\', description="it\'s a blaw blaw blaw blaw  blaw blaw ", workflow=\'Workflow_1\', project_type=\'Classic Software\', created_by=UserDto(user_id=1, username=\'username_1\', profile_pic=\'http://www.google.com\', phone_no=\'9999999999\', is_admin=True), created_at=\'2020-05-28 10:06:23\', developer_ids=[])')

snapshots['TestProjectStorage.test_get_user_projects_count projects_count'] = 2

snapshots['TestProjectStorage.test_get_user_projects_count_with_no_projects projects_count'] = 0

snapshots['TestProjectStorage.test_get_admin_projects_count projects_count'] = 2

snapshots['TestProjectStorage.test_get_admin_projects_count_with_no_projects projects_count'] = 0

snapshots['TestProjectStorage.test_validate_transition_with_valid_transition is_transition_valid'] = True

snapshots['TestProjectStorage.test_validate_transition_with_invalid_transition is_transition_valid'] = False

snapshots['TestProjectStorage.test_get_projects_for_user user_projects_details'] = [
    GenericRepr('ProjectDetailsDto(project_id=1, name=\'projectManagement\', description="it\'s a blaw blaw blaw blaw  blaw blaw ", workflow=\'Workflow_1\', project_type=\'Classic Software\', created_by=UserDto(user_id=1, username=\'username_1\', profile_pic=\'http://www.google.com\', phone_no=\'9999999999\', is_admin=True), created_at=\'2020-05-28 10:06:23\', developer_ids=[1, 2])'),
    GenericRepr('ProjectDetailsDto(project_id=2, name=\'projectManagement_2\', description="it\'s a blaw blaw blaw blaw  blaw blaw ", workflow=\'Workflow_1\', project_type=\'Classic Software\', created_by=UserDto(user_id=1, username=\'username_1\', profile_pic=\'http://www.google.com\', phone_no=\'9999999999\', is_admin=True), created_at=\'2020-05-28 10:06:23\', developer_ids=[2])')
]

snapshots['TestProjectStorage.test_get_projects_for_user_with_limit_1 user_projects_details'] = [
    GenericRepr('ProjectDetailsDto(project_id=1, name=\'projectManagement\', description="it\'s a blaw blaw blaw blaw  blaw blaw ", workflow=\'Workflow_1\', project_type=\'Classic Software\', created_by=UserDto(user_id=1, username=\'username_1\', profile_pic=\'http://www.google.com\', phone_no=\'9999999999\', is_admin=True), created_at=\'2020-05-28 10:06:23\', developer_ids=[1, 2])')
]

snapshots['TestProjectStorage.test_get_projects_for_user_with_offset_1 user_projects_details'] = [
    GenericRepr('ProjectDetailsDto(project_id=2, name=\'projectManagement_2\', description="it\'s a blaw blaw blaw blaw  blaw blaw ", workflow=\'Workflow_1\', project_type=\'Classic Software\', created_by=UserDto(user_id=1, username=\'username_1\', profile_pic=\'http://www.google.com\', phone_no=\'9999999999\', is_admin=True), created_at=\'2020-05-28 10:06:23\', developer_ids=[2])')
]

snapshots['TestProjectStorage.test_get_projects_for_user_with_offset_gt_total_ptojects user_projects_details'] = [
]

snapshots['TestProjectStorage.test_get_projects_for_admin user_projects_details'] = [
    GenericRepr('ProjectDetailsDto(project_id=1, name=\'projectManagement\', description="it\'s a blaw blaw blaw blaw  blaw blaw ", workflow=\'Workflow_1\', project_type=\'Classic Software\', created_by=UserDto(user_id=1, username=\'username_1\', profile_pic=\'http://www.google.com\', phone_no=\'9999999999\', is_admin=True), created_at=\'2020-05-28 10:06:23\', developer_ids=[1, 2])'),
    GenericRepr('ProjectDetailsDto(project_id=2, name=\'projectManagement_2\', description="it\'s a blaw blaw blaw blaw  blaw blaw ", workflow=\'Workflow_1\', project_type=\'Classic Software\', created_by=UserDto(user_id=1, username=\'username_1\', profile_pic=\'http://www.google.com\', phone_no=\'9999999999\', is_admin=True), created_at=\'2020-05-28 10:06:23\', developer_ids=[2])')
]

snapshots['TestProjectStorage.test_get_projects_for_admin_with_limit_1 user_projects_details'] = [
    GenericRepr('ProjectDetailsDto(project_id=1, name=\'projectManagement\', description="it\'s a blaw blaw blaw blaw  blaw blaw ", workflow=\'Workflow_1\', project_type=\'Classic Software\', created_by=UserDto(user_id=1, username=\'username_1\', profile_pic=\'http://www.google.com\', phone_no=\'9999999999\', is_admin=True), created_at=\'2020-05-28 10:06:23\', developer_ids=[1, 2])')
]

snapshots['TestProjectStorage.test_get_projects_for_admin_with_offset_1 user_projects_details'] = [
    GenericRepr('ProjectDetailsDto(project_id=2, name=\'projectManagement_2\', description="it\'s a blaw blaw blaw blaw  blaw blaw ", workflow=\'Workflow_1\', project_type=\'Classic Software\', created_by=UserDto(user_id=1, username=\'username_1\', profile_pic=\'http://www.google.com\', phone_no=\'9999999999\', is_admin=True), created_at=\'2020-05-28 10:06:23\', developer_ids=[2])')
]

snapshots['TestProjectStorage.test_get_projects_for_admin_with_offset_gt_total_projects user_projects_details'] = [
]

snapshots['TestProjectStorage.test_get_workflow_id_of_project workflow_id'] = 1

snapshots['TestProjectStorage.test_get_states_transition_details transition_details_dto'] = GenericRepr("TransitionDetailsDto(name='transition_1', from_state=StateDetailsDto(state_id=1, name='State_1'), to_state=StateDetailsDto(state_id=2, name='State_2'), checklist=[ChecklistDetailsDto(checklist_id=1, name='Check_1', is_required=True), ChecklistDetailsDto(checklist_id=2, name='Check_2', is_required=False), ChecklistDetailsDto(checklist_id=3, name='Check_3', is_required=True), ChecklistDetailsDto(checklist_id=4, name='Check_4', is_required=False)], description='some content')")

snapshots['TestProjectStorage.test_get_states_transition_details_with_zero_checklist transition_details'] = GenericRepr("TransitionDetailsDto(name='transition_3', from_state=StateDetailsDto(state_id=1, name='State_1'), to_state=StateDetailsDto(state_id=3, name='State_3'), checklist=[], description='some content')")

snapshots['TestProjectStorage.test_get_transition_mandatory_checklist transition_checklist_dtos'] = [
    GenericRepr("ChecklistDetailsDto(checklist_id=1, name='Check_1', is_required=True)"),
    GenericRepr("ChecklistDetailsDto(checklist_id=3, name='Check_3', is_required=True)")
]

snapshots['TestProjectStorage.test_get_transition_mandatory_checklist_with_empty transition_checklist'] = [
]

snapshots['TestProjectStorage.test_validate_project_id_with_valid_id project_dto'] = GenericRepr('ProjectDto(name=\'projectManagement\', description="it\'s a blaw blaw blaw blaw  blaw blaw ", workflow_id=1, project_type=\'Classic Software\', developer_ids=None)')

snapshots['TestProjectStorage.test_validate_project_id_with_invalid_id project_dto'] = None
