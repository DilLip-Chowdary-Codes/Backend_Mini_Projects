from project_management_portal.dtos\
  import ProjectDto, UserDto, ProjectDetailsDto,\
      StateDto, TaskDetailsDto, TaskDto, ChecklistDetailsDto,\
      GetTransitionDetailsDto, UpdateTransitionInputDto,\
      ChecklistStatusDto

project_data = {
  "project_id":1,
  "name": "projectManagement",
  "description": "it's a blaw blaw blaw blaw  blaw blaw ",
  "workflow_id": 1,
  "project_type": "Classic Software",
  "developers": [1]
}

user_dto = UserDto(
  user_id=1,
  username="username_1",
  profile_pic="http://www.google.com",
  phone_no="9782346742",
  is_admin=True)

project_dto = ProjectDto(
            name=project_data.get('name'),
            description=project_data.get('description'),
            workflow_id=project_data.get('workflow_id'),
            project_type=project_data.get('project_type'),
            developers=project_data.get('developers')
            )
project_with_no_developers_dto = ProjectDto(
            name=project_data.get('name'),
            description=project_data.get('description'),
            workflow_id=project_data.get('workflow_id'),
            project_type=project_data.get('project_type'),
            developers=[]
            )

projects_dtos =[
  ProjectDto(
    name=project_data.get('name'),
    description=project_data.get('description'),
    workflow_id=project_data.get('workflow_id'),
    project_type=project_data.get('project_type'),
    developers=project_data.get('developers')
    )
    ]

project_details_dto = ProjectDetailsDto(
    project_id=1,
    name="projectManagement",
    description="it's a blaw blaw blaw blaw  blaw blaw ",
    workflow="Workflow_1",
    project_type="Classic Software",
    created_by=user_dto,
    created_at="2020-05-28 10:06:23",
    developers= [user_dto])

project_details_with_no_developers_dto = ProjectDetailsDto(
    project_id=1,
    name="projectManagement",
    description="it's a blaw blaw blaw blaw  blaw blaw ",
    workflow="Workflow_1",
    project_type="Classic Software",
    created_by=user_dto,
    created_at="2020-05-28 10:06:23",
    developers= [])

projects_details_dtos = [project_details_dto]


task_data = {
  "project_id": 1,
  "issue_type": "Enhancement",
  "title": "Optimizing DB",
  "description": "string",
  "state_id": 1
}

task_user_dto = UserDto(
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

task_project_dto = ProjectDetailsDto(
  project_id=1,
  name="projectManagement",
  description="it's a blaw blaw blaw blaw  blaw blaw ",
  workflow="",
  project_type="Classic Software",
  created_by=user_dto,
  created_at="2020-05-28 10:06:23",
  developers=[developer_dto]
  )

task_dto = TaskDto(
  project_id=1,
    issue_type="Enhancement",
    title="Optimizing DB",
    description="string",
    state_id=1)

task_details_dto = TaskDetailsDto(
  task_id=1,
  project=task_project_dto,
  issue_type="Enhancement",
  title="Optimizing DB",
  assignee=task_user_dto,
  description="string",
  state=state_dto
  )

tasks_dtos = [task_dto]
tasks_details_dtos = [task_details_dto]

from_state_id = task_dto.state_id
transition_details_query_dict = {
        "user_id": 1,
        "project_id": 1,
        "task_id": 1,
        "to_state_id": 2
    }

get_transition_details_query_dto = GetTransitionDetailsDto(
            project_id=transition_details_query_dict['project_id'],
            task_id=transition_details_query_dict['task_id'],
            from_state_id=from_state_id,
            to_state_id=transition_details_query_dict['to_state_id']
            )

query_dto_with_no_checklist_for_transition = GetTransitionDetailsDto(
            project_id=transition_details_query_dict['project_id'],
            task_id=transition_details_query_dict['task_id'],
            from_state_id=1,
            to_state_id=3
            )

checklist_status_dtos = [
  ChecklistStatusDto(
    checklist_id=1,
    is_checked=True
  ),
  ChecklistStatusDto(
    checklist_id=1,
    is_checked=False
  )
  ]

update_task_state_query_dto = UpdateTransitionInputDto(
  project_id=1,
  task_id=1,
  from_state_id=1,
  to_state_id=2,
  checklist=checklist_status_dtos
  )
  
update_task_state_query_expected_empty_checklist_dto\
  = UpdateTransitionInputDto(
    project_id=1,
    task_id=1,
    from_state_id=1,
    to_state_id=3,
    checklist=[]
    )
