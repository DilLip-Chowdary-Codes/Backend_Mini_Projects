from datetime import datetime
from common.dtos import UserAuthTokensDTO
from project_management_portal.dtos\
  import UserDto, ProjectDto,\
         ProjectDetailsDto, TransitionDto,\
         StateDto, TaskDetailsDto, WorkflowDetailsDto,\
         TransitionDetailsDto, ChecklistDetailsDto,\
         GetTransitionDetailsDto, StateDetailsDto

from .raw_inputs import project_data, project_details_dto,user_dto


access_token_dto = UserAuthTokensDTO(
  user_id=1,
  access_token="testing_access_token",
  refresh_token="testing_refresh_token",
  expires_in=10000000
  )

valid_login_response = {
            "user_id": 1,
            "username": "username_1",
            "profile_pic": "http://www.google.com/",
            "is_admin": True,
            "access_token":"testing_access_token",
            "refresh_token":"testing_refresh_token",
            "expires_in":10000000
        }

user_details = {
  "user_id": 1,
  "username":"username_1",
  "profile_pic":"http://www.google.com/",
  "phone_no": "8739835635"
}

developer_details = {
  "user_id": 2,
  "username":"username_2",
  "profile_pic":"http://www.google.com/",
  "phone_no": "8739835635"
}

create_project_response = {
  "name": "projectManagement",
  "description": "it's a blaw blaw blaw blaw  blaw blaw ",
  "workflow": "",
  "project_type": "Classic Software",
  "created_by": user_details,
  "created_at": "2020-05-28 10:06:23",
  "developers": [developer_details]
}

get_projects_response = [
  {
    "name": "projectManagement",
    "description": "it's a blaw blaw blaw blaw  blaw blaw ",
    "workflow": "",
    "project_type": "Classic Software",
    "created_by": user_details,
    "created_at": "2020-05-28 10:06:23",
    "developers": [developer_details]
  }
  ]

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

task_details_response = {
  "project": create_project_response,
  "issue_type": "Enhancement",
  "title":"Optimizing DB",
  "assignee_id": user_details['user_id'],
  "description":"string",
  "state": "In Progress"
}

tasks_details_response = {
  "total_tasks": 1,
  "tasks":[task_details_response]
}

update_task_state_data = {
  
  "user_id": 1,
  "project_id": 1,
  "task_id": 1,
  "from_state_id": 1,
  "to_state_id": 2
}

updated_task_details_response = {
  "project": create_project_response,
  "issue_type": "Enhancement",
  "title":"Optimizing DB",
  "assignee_id": user_details['user_id'],
  "description":"string",
  "state": "In Progress"
}

states_dto = [
  StateDto(
  name="State_1"),
  StateDto(
  name="State_2"),
  StateDto(
  name="State_3"),
  ]

state_2_dto = StateDto(
  name="New State")

updated_task_details_dto = TaskDetailsDto(
  task_id=1,
  project=project_details_dto,
  issue_type="Enhancement",
  title="Optimizing DB",
  assignee_id=user_dto.user_id,
  description="string",
  state=state_2_dto
  )


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

project_details_dto = ProjectDetailsDto(
  project_id=1,
  name="projectManagement",
  description="it's a blaw blaw blaw blaw  blaw blaw ",
  workflow="",
  project_type="Classic Software",
  created_by_id=user_dto.user_id,
  created_at="2020-05-28 10:06:23",
  developer_ids=[developer_dto]
  )

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
            )
  ]

transitions_dtos_2 = [
  TransitionDto(
            name="transition_1",
            from_state_id=1,
            to_state_id=3,
            description="some content"
            ),
  TransitionDto(
            name="transition_2",
            from_state_id=3,
            to_state_id=2,
            description="some content"
            )
  ]

transitions_dtos_invalid = [
  TransitionDto(
            name="transition_1",
            from_state_id=2,
            to_state_id=1,
            description="some content"
            ),
  TransitionDto(
            name="transition_2",
            from_state_id=2,
            to_state_id=3,
            description="some content"
            )
  ]

workflows_details_dtos = [
  WorkflowDetailsDto(
    workflow_id=1,
    name="workflow_1",
    states=states_dto,
    transitions=transitions_dtos,
    created_at="2020-05-28 10:06:23"
    ),
  WorkflowDetailsDto(
    workflow_id=2,
    name="workflow_2",
    states=states_dto,
    transitions=transitions_dtos_2,
    created_at="2020-05-28 10:06:23"
    )
    ]

workflows_details = [
  {
    "workflow_id":1,
    "name":"workflow_1"
  },
  {
    "workflow_id":2,
    "name":"workflow_2"
  }
  ]


checklist_details_dto_1 = ChecklistDetailsDto(
  checklist_id=1,
  name="Check_1",
  is_required=True)

checklist_details_dto_2 = ChecklistDetailsDto(
  checklist_id=2,
  name="Check_2",
  is_required=False)

checklist_details_dtos = [
  checklist_details_dto_1,
  checklist_details_dto_2
  ]

get_transition_details_dto = GetTransitionDetailsDto(
  project_id=1,
  task_id=1, 
  from_state_id=1,
  to_state_id=2)

transitions_details_dtos = TransitionDetailsDto(
  name="transition_1",
  from_state="State_1",
  to_state="State_2",
  description=None,
  checklist=checklist_details_dtos
  )

transition_details_response = {
  "task_id": 1,
  "from_state": {
    "state_id": 1,
    "name": "State_1"
  },
  "to_state": {
    "state_id": 2,
    "name": "State_2"
  },
  "check_list": [
    {
      "checklist_id": 1,
      "name": "Check_1",
      "is_required": True
    },
    {
      "checklist_id": 2,
      "name": "Check_2",
      "is_required": False
    }
  ]
}

available_states_dtos = [
  StateDetailsDto(
            state_id=1,
            name="State_2"
            ),
  StateDetailsDto(
            state_id=1,
            name="State_3"
            )
  ]

get_states_response={
  "total_states": 2,
  "states": [
    {
      "state_id": 2,
      "name": "State_2"
    },
    {
      "state_id": 3,
      "name": "State_3"
    }
  ]
}

mandatory_checklist_dtos = [checklist_details_dto_1]
