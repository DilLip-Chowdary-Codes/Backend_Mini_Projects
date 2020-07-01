from project_management_portal.dtos\
  import \
    ProjectDto, UserDto,\
    ProjectDetailsDto, TaskDetailsDto,\
    StateDto, StateDetailsDto, WorkflowDetailsDto,\
    TransitionDetailsDto

project_data = {
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
  phone_no="8739835635",
  is_admin=True
  )

project_dto = ProjectDto(
            name=project_data.get('name'),
            description=project_data.get('description'),
            workflow_id=project_data.get('workflow_id'),
            project_type=project_data.get('project_type'),
            developer_ids=project_data.get('developers')
            )

projects_dtos =[
  ProjectDto(
    name=project_data.get('name'),
    description=project_data.get('description'),
    workflow_id=project_data.get('workflow_id'),
    project_type=project_data.get('project_type'),
    developer_ids=project_data.get('developers')
    )
    ]

project_details_dto = ProjectDetailsDto(
    project_id=1,
    name="projectManagement",
    description="it's a blaw blaw blaw blaw  blaw blaw ",
    workflow="type",
    project_type="Classic Software",
    created_by=user_dto,
    created_at="2020-05-28 10:06:23 AM",
    developer_ids=[user_dto.user_id])

projects_details_dtos = [project_details_dto]

state_dto = StateDto(
  name="In Progress")


state_dto_1 = StateDto(
name="State_1")

state_dto_2 = StateDto(
name="State_2")

task_user_dto = UserDto(
  user_id=1,
  username="username_1",
  profile_pic="http://www.google.com/",
  phone_no="8739835635",
  is_admin=False
  )

task_developer_dto = UserDto(
  user_id=2,
  username="username_2",
  profile_pic="http://www.google.com/",
  phone_no="8739835635",
  is_admin=False
  )

developer_dto = UserDto(
  user_id=2,
  username="username_2",
  profile_pic="http://www.google.com/",
  phone_no="8739835635",
  is_admin=False
  )

task_project_dto = ProjectDetailsDto(
  project_id=1,
  name="projectManagement",
  description="it's a blaw blaw blaw blaw  blaw blaw ",
  workflow="",
  project_type="Classic Software",
  created_by=task_user_dto,
  created_at="2020-05-28 10:06:23",
  developer_ids=[developer_dto.user_id]
  )

task_details_dto = TaskDetailsDto(
  task_id=1,
  project=task_project_dto,
  issue_type="Enhancement",
  title="Optimizing DB",
  assignee_id=task_user_dto,
  description="string",
  state=state_dto.name
  )

tasks_details_dtos = [task_details_dto]

transition_dto = TransitionDetailsDto(
  name="transition_1",
  from_state="State_1",
  to_state="State_2",
  description="string",
  checklist=[]
  )

transition_dto_2 = TransitionDetailsDto(
  name="transition_2",
  from_state="State_1",
  to_state="State_2",
  description="string",
  checklist=[]
  )

workflow_details_dto_1 = WorkflowDetailsDto(
  workflow_id=1,
  name="workflow_1",
  states=[state_dto_1, state_dto_2],
  transitions=[transition_dto, transition_dto_2],
  created_at="2020-05-28 10:06:23"
  )

workflow_details_dto_2 = WorkflowDetailsDto(
  workflow_id=2,
  name="workflow_2",
  states=[state_dto_1, state_dto_2],
  transitions=[transition_dto, transition_dto_2],
  created_at="2020-05-28 10:06:23"
  )

workflow_details_dtos = [workflow_details_dto_1, workflow_details_dto_2]
workflow_details_dtos_empty = []

states_details_dtos = [
  StateDetailsDto(
    state_id=1,
    name="State_1"
    ),
  StateDetailsDto(
    state_id=2,
    name="State_2"
    )
  ]

states_details_dtos_empty = []
