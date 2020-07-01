# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestWorkFlowStorage.test_get_workflows workflow_details_dtos'] = [
    GenericRepr("WorkflowDetailsDto(workflow_id=1, name='Workflow_1', states=[StateDto(name='State_1'), StateDto(name='State_2'), StateDto(name='State_3')], transitions=[TransitionDetailsDto(name='transition_1', from_state='State_1', to_state='State_2', checklist=[ChecklistDetailsDto(checklist_id=1, name='Check_1', is_required=True), ChecklistDetailsDto(checklist_id=2, name='Check_2', is_required=False), ChecklistDetailsDto(checklist_id=3, name='Check_3', is_required=True), ChecklistDetailsDto(checklist_id=4, name='Check_4', is_required=False)], description='some content'), TransitionDetailsDto(name='transition_2', from_state='State_2', to_state='State_3', checklist=[ChecklistDetailsDto(checklist_id=1, name='Check_1', is_required=True), ChecklistDetailsDto(checklist_id=2, name='Check_2', is_required=False), ChecklistDetailsDto(checklist_id=3, name='Check_3', is_required=True), ChecklistDetailsDto(checklist_id=4, name='Check_4', is_required=False)], description='some content'), TransitionDetailsDto(name='transition_3', from_state='State_1', to_state='State_3', checklist=[], description='some content')], created_at='2020-05-28 10:06:23')"),
    GenericRepr("WorkflowDetailsDto(workflow_id=2, name='Workflow_2', states=[], transitions=[], created_at='2020-05-28 10:06:23')")
]

snapshots['TestWorkFlowStorage.test_get_workflows_with_no_workflows workflow_details_dtos'] = [
]

snapshots['TestWorkFlowStorage.test_get_workflows_with_no_states workflow_details_dtos'] = [
    GenericRepr("WorkflowDetailsDto(workflow_id=1, name='Workflow_1', states=[], transitions=[TransitionDetailsDto(name='transition_1', from_state='State_1', to_state='State_2', checklist=[ChecklistDetailsDto(checklist_id=1, name='Check_1', is_required=True), ChecklistDetailsDto(checklist_id=2, name='Check_2', is_required=False), ChecklistDetailsDto(checklist_id=3, name='Check_3', is_required=True), ChecklistDetailsDto(checklist_id=4, name='Check_4', is_required=False)], description='some content'), TransitionDetailsDto(name='transition_2', from_state='State_2', to_state='State_3', checklist=[ChecklistDetailsDto(checklist_id=1, name='Check_1', is_required=True), ChecklistDetailsDto(checklist_id=2, name='Check_2', is_required=False), ChecklistDetailsDto(checklist_id=3, name='Check_3', is_required=True), ChecklistDetailsDto(checklist_id=4, name='Check_4', is_required=False)], description='some content'), TransitionDetailsDto(name='transition_3', from_state='State_1', to_state='State_3', checklist=[], description='some content')], created_at='2020-05-28 10:06:23')"),
    GenericRepr("WorkflowDetailsDto(workflow_id=2, name='Workflow_2', states=[], transitions=[], created_at='2020-05-28 10:06:23')")
]

snapshots['TestWorkFlowStorage.test_get_workflows_with_no_transitions workflow_details_dtos'] = [
    GenericRepr("WorkflowDetailsDto(workflow_id=1, name='Workflow_1', states=[StateDto(name='State_1'), StateDto(name='State_2'), StateDto(name='State_3')], transitions=[], created_at='2020-05-28 10:06:23')"),
    GenericRepr("WorkflowDetailsDto(workflow_id=2, name='Workflow_2', states=[], transitions=[], created_at='2020-05-28 10:06:23')")
]
