from typing import  Optional, List
from dataclasses import dataclass

@dataclass
class UserDto:
    user_id: int
    username: str
    profile_pic: str
    phone_no: str
    is_admin: bool

@dataclass
class ProjectDto:
    name: str
    description: str
    workflow_id: int
    project_type: str
    developer_ids: Optional[List[int]] = None

@dataclass
class ProjectDetailsDto:
    project_id: int
    name: str
    description: str
    workflow: str
    project_type: str
    created_by_id: int
    created_at: str
    developer_ids: List[int]

@dataclass
class StateDto:
    name: str

@dataclass
class StateDetailsDto:
    state_id: int
    name: str

@dataclass
class TaskDto:
    project_id: int
    issue_type: str
    title: str
    description: str
    state_id: int

@dataclass
class TaskDetailsDto:
    task_id: int
    project: ProjectDetailsDto
    issue_type: str
    title: str
    assignee_id: int
    description: str
    state: str

@dataclass
class TransitionDto:
    name: str
    from_state_id: int
    to_state_id: int
    description: Optional[str] = None

@dataclass
class ChecklistDetailsDto:
    checklist_id: int
    name: str
    is_required: bool

@dataclass
class TransitionDetailsDto:
    name: str
    from_state: str
    to_state: str
    checklist: List[ChecklistDetailsDto]
    description: Optional[str] = None

@dataclass
class WorkflowDetailsDto:
    workflow_id: int
    name: str
    states: List[StateDto]
    transitions: List[TransitionDto]
    created_at: str

@dataclass
class GetTransitionDetailsDto:
    project_id: int
    task_id: int
    from_state_id: int
    to_state_id: int

@dataclass
class ChecklistStatusDto:
    checklist_id: int
    is_checked: bool

@dataclass
class UpdateTransitionInputDto:
    project_id: int
    task_id: int
    from_state_id: int
    to_state_id: int
    checklist: List[ChecklistStatusDto]
