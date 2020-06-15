from abc import ABC
from abc import abstractmethod

from project_management_portal.dtos\
    import ProjectDetailsDto

class ProjectPresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_workflow_id_exception(self):
        pass

    @abstractmethod
    def raise_invalid_project_id_exception(self):
        pass

    @abstractmethod
    def raise_invalid_transition_exception(self):
        pass

    @abstractmethod
    def raise_unauthorized_developer_exception(self):
        pass

    @abstractmethod
    def get_project_details_response(
            self,
            project_details_dto: ProjectDetailsDto
            ):
        pass

    @abstractmethod
    def get_projects_response(self,
                              total_projects_count,
                              all_projects_details_dtos):
        pass

    @abstractmethod
    def get_transition_details_response(self, transition_details_dtos):
        pass

    @abstractmethod
    def raise_checklist_not_satisfied_exception(self):
        pass

    @abstractmethod
    def raise_invalid_limit_value_exception(self):
        pass

    @abstractmethod
    def raise_invalid_offset_value_exception(self):
        pass
