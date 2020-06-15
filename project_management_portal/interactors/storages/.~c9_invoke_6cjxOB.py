from abc import ABC, abstractmethod
from typing import  Optional, List
from common.dtos import UserAuthTokensDTO
from project_management_portal.dtos import ProjectDto

class ProjectStorageInterface(ABC):

    @abstractmethod
    def validate_workflow_id(self, workflow_id: int) -> bool:
        pass

    @abstractmethod
    def validate_admin_scope(self, user_id: int):
        pass

    @abstractmethod
    def validate_project_id(self, project_id: int):
        pass
    
    @abstractmethod
    def validate_state_transition(self,
                                  workflow_id: int,
                                  from_state_id: int,
                                  to_state_id: int):
        pass

    @abstractmethod
    def validate_developer_for_project(
        self,
        user_id: int,
        project_id: int
        ) -> bool:

        pass

    @abstractmethod
    def create_project(self, user_id: int, project_dto: ProjectDto) -> int:
        pass

    @abstractmethod
    def get_projects_involved_by_user(self,
                                      user_id: int) -> List[ProjectDto]:
        pass

    @abstractmethod
    def get_projects_created_by_user(self,
                                     user_id: int) -> List[ProjectDto]:
        pass

    @abstractmethod
    def get_transitions_of_workflow(
        self,
        workflow_id: int
        ):

        pass
    
    @abstractmethod
    def validate_transition(self, workflow_id: int,
                            from_state_id: int, to_state_id: int):
        pass

    @abstractmethod
    def get_workflow_id_of_project(self, project_id: int) -> int:
        pass

    @abstractmethod
    def get_states_transition_details(self, get_transition_details_query_dto):
        pass
    
    @abstractmethod
    def validate_checklists(self, checklist_dtos):
        pass
