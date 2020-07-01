from abc import ABC, abstractmethod
from typing import  Optional, List
from common.dtos import UserAuthTokensDTO
from project_management_portal.dtos import ProjectDto

class ProjectStorageInterface(ABC):

    @abstractmethod
    def validate_workflow_id(self, workflow_id: int) -> bool:
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
    def get_projects_for_user(self,
                                      user_id: int,
                                      offset: int,
                                      limit: int) -> List[ProjectDto]:
        pass

    @abstractmethod
    def get_projects_for_admin(self,
                                     user_id: int,
                                     offset: int,
                                     limit: int) -> List[ProjectDto]:
        pass

    @abstractmethod
    def get_user_projects_count(self, user_id):
        pass

    @abstractmethod
    def get_admin_projects_count(self, user_id):
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
    def get_transition_mandatory_checklist(
            self, update_task_state_query_dto):
        pass
