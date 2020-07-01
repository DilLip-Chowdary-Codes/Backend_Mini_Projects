from datetime import datetime
from .raw_inputs import project_data
from user_app.dtos\
  import ProjectDto, UserDto, ProjectDetailsDto,\
      StateDto, StateDetailsDto,\
      TaskDetailsDto, TaskDto, TransitionDto,\
      TransitionDetailsDto, WorkflowDetailsDto, ChecklistDetailsDto

valid_login_response = {
            "access_token":"testing_access_token",
            "refresh_token":"testing_refresh_token",
            "expires_in":datetime.now()
        }

project_dto = ProjectDto(
  name="projectManagement",
  description="it's a blaw blaw blaw blaw  blaw blaw ",
  workflow_id=1,
  project_type="Classic Software",
  developer_ids=[]
  )

get_project_response = {
  "project_id":1,
  "name": "projectManagement",
  "description": "it's a blaw blaw blaw blaw  blaw blaw ",
  "workflow": "Workflow_1",
  "project_type": "Classic Software",
  "created_by": {
      "user_id": 1,
      "username": "username_1",
      "profile_pic": "http://www.google.com",
      "phone_no": "9782346742"
    },
  "created_at": "2020-05-28 10:06:23 AM",
  "developers": [
    {
      "user_id": 1,
      "username": "username_1",
      "profile_pic": "http://www.google.com",
      "phone_no": "9782346742"
    }
  ]
}

get_projects_response = [
  {
  "project_id":1,
  "name": "projectManagement",
  "description": "it's a blaw blaw blaw blaw  blaw blaw ",
  "workflow": "type",
  "project_type": "Classic Software",
  "created_by": {
      "user_id": 1,
      "username": "username_1",
      "profile_pic": "http://www.google.com",
      "phone_no": "9782346742"
    },
  "created_at": "2020-05-28 10:06:23 AM",
  "developers": [
    {
      "user_id": 1,
      "username": "username_1",
      "profile_pic": "http://www.google.com",
      "phone_no": "9782346742"
    }
  ]
},
{ "project_id":2,
  "name": "projectManagement_2",
  "description": "it's a blaw blaw blaw blaw  blaw blaw ",
  "workflow": "type",
  "project_type": "Classic Software",
  "created_by": {
      "user_id": 1,
      "username": "username_1",
      "profile_pic": "http://www.google.com",
      "phone_no": "9782346742"
    },
  "created_at": "2020-05-28 10:06:23 AM",
  "developers": [
    {
      "user_id": 1,
      "username": "username_1",
      "profile_pic": "http://www.google.com",
      "phone_no": "9782346742"
    },
    {
      "user_id": 2,
      "username": "username_2",
      "profile_pic": "http://www.google.com",
      "phone_no": "9782346742"
    }
  ]
}
]

user_dto = UserDto(
  user_id=1,
  username="username_1",
  profile_pic="http://www.google.com",
  phone_no="9782346742",
  is_admin=True
  )

user_dto_2 = UserDto(
  user_id=2,
  username="username_2",
  profile_pic="http://www.google.com",
  phone_no="9782346742",
  is_admin=False)

project_details_dto_1 = ProjectDetailsDto(
    project_id=1,
    name="projectManagement",
    description="it's a blaw blaw blaw blaw  blaw blaw ",
    workflow="Workflow_1",
    project_type="Classic Software",
    created_by=user_dto,
    created_at="2020-05-28 10:06:23",
    developer_ids= [user_dto.user_id, user_dto_2.user_id])

project_details_dto_2 = ProjectDetailsDto(
    project_id=2,
    name="projectManagement_2",
    description="it's a blaw blaw blaw blaw  blaw blaw ",
    workflow="Workflow_1",
    project_type="Classic Software",
    created_by=user_dto,
    created_at="2020-05-28 10:06:23",
    developer_ids= [user_dto_2.user_id])

user_projects_details_dtos = [
  project_details_dto_1,
  project_details_dto_2
  ]

state_dto = StateDto(
  name="State_1")

state_2_dto = StateDto(
  name="State_2")

state_3_dto = StateDto(
  name="State_3")

developer_dto = UserDto(
  user_id=1,
  username="username_1",
  profile_pic="http://www.google.com",
  phone_no="9782346742",
  is_admin=True
  )

developer_dto_2 = UserDto(
  user_id=2,
  username="username_2",
  profile_pic="http://www.google.com",
  phone_no="9782346742",
  is_admin=False
  )

task_project_dto = ProjectDetailsDto(
  project_id=1,
  name="projectManagement",
  description="it's a blaw blaw blaw blaw  blaw blaw ",
  workflow="Workflow_1",
  project_type="Classic Software",
  created_by=user_dto,
  created_at="2020-05-28 10:06:23",
  developer_ids=[developer_dto.user_id, developer_dto_2.user_id]
  )

task_user_dto = UserDto(
  user_id=1,
  username="username_1",
  profile_pic="http://www.google.com",
  phone_no="9782346742",
  is_admin=True
  )

task_2_user_dto = UserDto(
  user_id=2,
  username="username_2",
  profile_pic="http://www.google.com",
  phone_no="9782346742",
  is_admin=False
  )

task_details_dto = TaskDetailsDto(
  task_id=1,
  project=task_project_dto,
  issue_type="Enhancement",
  title="Optimizing DB",
  assignee=task_user_dto,
  description="string",
  state=state_dto.name
  )

task_2_details_dto = TaskDetailsDto(
  task_id=2,
  project=task_project_dto,
  issue_type="BUG",
  title="Optimizing DB",
  assignee=task_2_user_dto,
  description="string",
  state=state_2_dto.name
  )

tasks_details_dtos = [task_2_details_dto, task_details_dto]

user_details = {
  "user_id":1,
  "username":"username_1",
  "profile_pic":"http://www.google.com",
  "phone_no":"9782346742"
}

user_details_2 = {
  "user_id":2,
  "username":"username_2",
  "profile_pic":"http://www.google.com",
  "phone_no":"9782346742"
}

project_details = {
    "name": "projectManagement",
    "description": "it's a blaw blaw blaw blaw  blaw blaw ",
    "workflow": "Workflow_1",
    "project_type": "Classic Software",
    "created_by": user_details,
    "created_at": "2020-05-28 10:06:23",
    "developers": [user_details, user_details_2]
  }

task_details_response = {
  "project": project_details,
  "issue_type": "Enhancement",
  "title":"Optimizing DB",
  "assignee": user_details,
  "description":"string",
  "state": "In Progress"
}

tasks_details_response = {
  "total_tasks": 1,
  "tasks":[task_details_response]
}

transitions_dtos = [
  TransitionDto(
            name="transition_1",
            from_state_id=1,
            to_state_id=2,
            description="some content"
            ),
  TransitionDto(
            name="transition_2",
            from_state_id=2,
            to_state_id=3,
            description="some content"
            ),
  TransitionDto(
            name="transition_3",
            from_state_id=1,
            to_state_id=3,
            description="some content"
            )
  ]
checklist_details_dtos = [
  ChecklistDetailsDto(
    checklist_id=1,
    name="Check_1",
    is_required=True),
  ChecklistDetailsDto(
    checklist_id=2,
    name="Check_2",
    is_required=False)
  ]

transition_details_dtos = [
  TransitionDetailsDto(
    name="transition_1",
    from_state="State_1",
    to_state="State_2",
    description="some content",
    checklist=checklist_details_dtos
    ),
  TransitionDetailsDto(
    name="transition_2",
    from_state="State_2",
    to_state="State_3",
    description="some content",
    checklist=checklist_details_dtos
    ),
  TransitionDetailsDto(
    name="transition_3",
    from_state="State_1",
    to_state="State_3",
    description="some content",
    checklist=[]
    )
  ]

state_details_dtos = [
  StateDto(
    name="State_1"),
  StateDto(
    name="State_2"),
  StateDto(
    name="State_3")
  ]

workflow_details_dtos = [
  WorkflowDetailsDto(
    workflow_id=1,
    name="Workflow_1",
    states=state_details_dtos,
    transitions=transition_details_dtos,
    created_at="2020-05-28 10:06:23"
    ),
  WorkflowDetailsDto(
    workflow_id=2,
    name="Workflow_2",
    states=[],
    transitions=[],
    created_at="2020-05-28 10:06:23"
    )
  ]

workflow_details_dtos_with_no_states = [
  WorkflowDetailsDto(
    workflow_id=1,
    name="Workflow_1",
    states=[],
    transitions=transition_details_dtos,
    created_at="2020-05-28 10:06:23"
    ),
  WorkflowDetailsDto(
    workflow_id=2,
    name="Workflow_2",
    states=[],
    transitions=[],
    created_at="2020-05-28 10:06:23"
    )
  ]


workflow_details_dtos_with_no_transitions = [
  WorkflowDetailsDto(
    workflow_id=1,
    name="Workflow_1",
    states=state_details_dtos,
    transitions=[],
    created_at="2020-05-28 10:06:23"
    ),
  WorkflowDetailsDto(
    workflow_id=2,
    name="Workflow_2",
    states=[],
    transitions=[],
    created_at="2020-05-28 10:06:23"
    )
  ]

available_states_dtos = [
  StateDetailsDto(
    state_id=2,
    name="State_2"),
  StateDetailsDto(
    state_id=3,
    name="State_3")
  ]

available_states_dtos_empty = []

from_state_dto = StateDetailsDto(
            state_id=1,
            name="State_1"
            )
to_state_dto = StateDetailsDto(
            state_id=2,
            name="State_2"
            )

transition_details_dto = TransitionDetailsDto(
            name="transition_1",
            from_state=from_state_dto,
            to_state=to_state_dto,
            checklist=checklist_details_dtos,
            description="some content"
            )
from_state_dto = StateDetailsDto(
            state_id=1,
            name="State_1"
            )
to_state_dto = StateDetailsDto(
            state_id=3,
            name="State_3"
            )
transition_details_with_no_checklist_dto = TransitionDetailsDto(
            name="transition_3",
            from_state=from_state_dto,
            to_state=to_state_dto,
            checklist=[],
            description="some content"
            )

transition_checklist_dtos = [
  ChecklistDetailsDto(
            name="Check_1",
            is_required=True,
            checklist_id=1
            )
            ]

transition_checklist_empty_dtos = []
