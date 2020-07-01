from datetime import datetime
from .raw_inputs import project_data
from user_app.dtos\
  import ProjectDto

valid_login_response = {
            "access_token":"testing_access_token",
            "refresh_token":"testing_refresh_token",
            "expires_in":datetime.now()
        }

login_response = {
  "user_id":1,
  "username": "username_1",
  "profile_pic": "http://www.google.com",
  "is_admin": True,
  "access_token":"kjfewrfjbwg",
  "refresh_token":"sjdfbkgfsdg",
  "expires_in": '1000000'
        }

get_project_response = {
		"project_id": 1,
		"name": "projectManagement",
		"description": "it's a blaw blaw blaw blaw  blaw blaw ",
		"workflow": "type",
		"project_type": "Classic Software",
		"created_by": {
			"user_id": 1,
			"username": "username_1",
			"profile_pic": "http://www.google.com",
			"phone_no": "8739835635"
		},
		"created_at": "2020-05-28 10:06:23 AM",
		"developers": [{
			"user_id": 1,
			"username": "username_1",
			"profile_pic": "http://www.google.com",
			"phone_no": "8739835635"
		}]
		}
get_projects_response = {
	"total_projects": 1,
	"projects": [{
		"project_id": 1,
		"name": "projectManagement",
		"description": "it's a blaw blaw blaw blaw  blaw blaw ",
		"workflow": "type",
		"project_type": "Classic Software",
		"created_by": {
			"user_id": 1,
			"username": "username_1",
			"profile_pic": "http://www.google.com",
			"phone_no": "8739835635"
		},
		"created_at": "2020-05-28 10:06:23 AM",
		"developers": [{
			"user_id": 1,
			"username": "username_1",
			"profile_pic": "http://www.google.com",
			"phone_no": "8739835635"
		}]
	}]
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
  "project_id":1,
  "name": "projectManagement",
  "description": "it's a blaw blaw blaw blaw  blaw blaw ",
  "workflow": "",
  "project_type": "Classic Software",
  "created_by": user_details,
  "created_at": "2020-05-28 10:06:23",
  "developers": [developer_details]
}

# get_projects_response = [
#   {
#     "project_id":1,
#     "name": "projectManagement",
#     "description": "it's a blaw blaw blaw blaw  blaw blaw ",
#     "workflow": "",
#     "project_type": "Classic Software",
#     "created_by": user_details,
#     "created_at": "2020-05-28 10:06:23",
#     "developers": [developer_details]
#   }
#   ]

project_dto = ProjectDto(
            name=project_data.get('name'),
            description=project_data.get('description'),
            workflow_id=project_data.get('workflow_id'),
            project_type=project_data.get('project_type'),
            developers=project_data.get('developers')
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

task_details_response = {
  "task_id":1,
  "project": create_project_response,
  "issue_type": "Enhancement",
  "title":"Optimizing DB",
  "assignee": user_details,
  "description":"string",
  "state": "In Progress"
}

tasks_details_responses = {
  "task_id":1,
  "issue_type": "Enhancement",
  "title":"Optimizing DB",
  "assignee": user_details,
  "description":"string",
  "state": "In Progress"
}

tasks_details_response = {
  "total_tasks": 1,
  "project": create_project_response,
  "tasks":[tasks_details_responses]
}

workflow_basic_details_dict_1 = {
  "workflow_id":1,
  "name":"workflow_1"
}

workflow_basic_details_dict_2 = {
  "workflow_id":2,
  "name":"workflow_2"
}

workflow_details_dict = {
  "total_workflows":2,
  "workflows": [
    workflow_basic_details_dict_1,
    workflow_basic_details_dict_2
    ]
}
workflow_details_dict_empty = {
  "total_workflows":0,
  "workflows": []
}

states_details_dicts = [
  {
    "state_id":1,
    "name":"State_1"
  },
  {
    "state_id":2,
    "name":"State_2"
  }
  ]

task_states_response = {
  "total_states": 2,
  "states": states_details_dicts
}

task_states_response_empty = {
  "total_states": 0,
  "states": []
}
