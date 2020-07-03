from project_management_portal.dtos\
  import \
    CreateProjectRequestDto, UserDto,\
    ProjectsDetailsDto,\
    ProjectDto, TaskDetailsDto,\
    StateDto, StateDetailsDto, WorkflowDetailsDto,\
    TransitionDetailsDto

project_data = {
  "name": "projectManagement",
  "description": "it's a blaw blaw blaw blaw  blaw blaw ",
  "workflow_id": 1,
  "project_type": "Classic Software",
  "developers": [1, 2]
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

project_dto = CreateProjectRequestDto(
            name=project_data.get('name'),
            description=project_data.get('description'),
            workflow_id=project_data.get('workflow_id'),
            project_type=project_data.get('project_type'),
            developers_ids=project_data.get('developers')
            )

projects_dtos =[
  CreateProjectRequestDto(
    name=project_data.get('name'),
    description=project_data.get('description'),
    workflow_id=project_data.get('workflow_id'),
    project_type=project_data.get('project_type'),
    developers_ids=project_data.get('developers')
    )
    ]

project_dto = ProjectDto(
    project_id=1,
    name="projectManagement",
    description="it's a blaw blaw blaw blaw  blaw blaw ",
    workflow="Workflow_1",
    project_type="Classic Software",
    created_by_id=user_dto.user_id,
    created_at="2020-05-28 10:06:23 AM",
    developers_ids=[user_dto.user_id, developer_dto.user_id])

project_dto_2 = ProjectDto(
    project_id=2,
    name="projectManagement_2",
    description="it's a blaw blaw blaw blaw  blaw blaw ",
    workflow="Workflow_2",
    project_type="Classic Software",
    created_by_id=user_dto.user_id,
    created_at="2020-05-28 10:06:23 AM",
    developers_ids=[developer_dto.user_id])

project_dtos = [project_dto, project_dto_2]

user_dtos = [user_dto, developer_dto]

projects_details_dto = ProjectsDetailsDto(
  project_dtos=project_dtos,
  user_dtos=user_dtos)

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

task_project_dto = ProjectDto(
  project_id=1,
  name="projectManagement",
  description="it's a blaw blaw blaw blaw  blaw blaw ",
  workflow="",
  project_type="Classic Software",
  created_by_id=task_user_dto.user_id,
  created_at="2020-05-28 10:06:23",
  developers_ids=[developer_dto.user_id]
  )

task_details_dto = TaskDetailsDto(
  task_id=1,
  project=task_project_dto,
  issue_type="Enhancement",
  title="Optimizing DB",
  assignee_id=task_user_dto.user_id,
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
