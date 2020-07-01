from project_management_portal.dtos\
  import TaskDetailsDto, ProjectDto,\
        StateDto, UserDto, ProjectDetailsDto,\
        TaskDto, TransitionDetailsDto, ChecklistDetailsDto,\
        UpdateTransitionInputDto, ChecklistStatusDto

project_data = {
  "name": "projectManagement",
  "description": "it's a blaw blaw blaw blaw  blaw blaw ",
  "workflow_id": 1,
  "project_type": "Classic Software",
  "developers": [1]
}

task_data = {
  "project_id": 1,
  "issue_type": "Enhancement",
  "title": "Optimizing DB",
  "description": "string",
  "state_id": 1
}

user_dto = UserDto(
  user_id=1,
  username="username_1",
  profile_pic="http://www.google.com",
  phone_no="8739835635",
  is_admin=True
  )

developer_dto = UserDto(
  user_id=2,
  username="username_2",
  profile_pic="http://www.google.com",
  phone_no="8739835635",
  is_admin=False
  )

state_dto = StateDto(
  name="In Progress")

state_2_dto = StateDto(
  name="New State")


project_dto = ProjectDto(
  name="projectManagement",
  description="it's a blaw blaw blaw blaw  blaw blaw ",
  workflow_id=1,
  project_type="Classic Software",
  developer_ids=[1]
  )

project_details_dto = ProjectDetailsDto(
  project_id=1,
  name="projectManagement",
  description="it's a blaw blaw blaw blaw  blaw blaw ",
  workflow="",
  project_type="Classic Software",
  created_by=user_dto,
  created_at="2020-05-28 10:06:23",
  developer_ids=[developer_dto]
  )

task_dto = TaskDto(
  project_id=1,
    issue_type="Enhancement",
    title="Optimizing DB",
    description="string",
    state_id=1)

task_details_dto = TaskDetailsDto(
  task_id=1,
  project=project_details_dto,
  issue_type="Enhancement",
  title="Optimizing DB",
  assignee_id=user_dto,
  description="string",
  state=state_dto
  )


tasks_dtos = [task_dto]
tasks_details_dtos = [task_details_dto]

#task_transition

checklist_input_dict= {
      "checklist_id": 1,
      "is_checked": True
    }

checklist_input_dict_2 = {
      "checklist_id": 2,
      "is_checked": False
    }

checklist_input_dicts_list = [
  checklist_input_dict,
  checklist_input_dict_2]

checklist_input_dict_unsatisfied_1 = {
      "checklist_id": 1,
      "is_checked": False
    }

checklist_input_dicts_list_unsatisfied_mandatory_fields = [
  checklist_input_dict_unsatisfied_1,
  checklist_input_dict_2
  ]

checklist_status_dto = ChecklistStatusDto(
            checklist_id=checklist_input_dict['checklist_id'],
            is_checked=checklist_input_dict['is_checked'])


checklist_status_dto_2 = ChecklistStatusDto(
            checklist_id=checklist_input_dict_2['checklist_id'],
            is_checked=checklist_input_dict_2['is_checked'])

checklist_status_dtos_list = [
  checklist_status_dto, checklist_status_dto_2
  ]

checklist_status_dto_unsatisfied = ChecklistStatusDto(
            checklist_id=checklist_input_dict_unsatisfied_1['checklist_id'],
            is_checked=checklist_input_dict_unsatisfied_1['is_checked'])

checklist_status_dtos_list_unsatisfied_mandatory_fields = [
  checklist_status_dto_unsatisfied,
  checklist_status_dto_2
  ]

update_task_state_input_data = {

  "user_id": 1,
  "project_id": 1,
  "task_id": 1,
  "from_state_id": 1,
  "to_state_id": 2,
  "checklist": checklist_input_dicts_list
}
update_task_state_input_data_with_unchecked_mandatory_checklist = {
  "user_id": 1,
  "project_id": 1,
  "task_id": 1,
  "from_state_id": 1,
  "to_state_id": 2,
  "checklist": checklist_input_dicts_list_unsatisfied_mandatory_fields
  
}
transition_details_query_dict = {
  "project_id":1,
  "task_id":1,
  "to_state_id":2
}

task_state_data = {
        "user_id": 1,
        "project_id": 1,
        "task_id": 1
    }

from_state_id = task_dto.state_id


update_task_state_query_dto = UpdateTransitionInputDto(
            project_id=update_task_state_input_data['project_id'],
            task_id=update_task_state_input_data['task_id'],
            from_state_id=from_state_id,
            to_state_id=update_task_state_input_data['to_state_id'],
            checklist=checklist_status_dtos_list)

update_task_state_query_dto_with_unchecked_mandatory_checklist\
  = UpdateTransitionInputDto(
            project_id=\
              update_task_state_input_data_with_unchecked_mandatory_checklist[
              'project_id'],
            task_id=\
              update_task_state_input_data_with_unchecked_mandatory_checklist[
              'task_id'],
            from_state_id=from_state_id,
            to_state_id=\
              update_task_state_input_data_with_unchecked_mandatory_checklist[
              'to_state_id'],
            checklist=checklist_status_dtos_list_unsatisfied_mandatory_fields
            )
