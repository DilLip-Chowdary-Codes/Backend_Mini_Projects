from typing import Dict
from project_management_portal.interactors.storages.project_storage_interface\
    import ProjectStorageInterface
from project_management_portal.interactors.presenters\
    .project_presenter_interface import ProjectPresenterInterface
from project_management_portal.dtos import ProjectDto
from project_management_portal.exceptions import InvalidWorkFlow

class CreateProjectInteractor:
    def __init__(self,
                 storage: ProjectStorageInterface
                ):
        self.storage = storage
    
    def create_project_wrapper(self, user_id: int, project_data: Dict,
                               presenter: ProjectPresenterInterface):

        try:
            project_details_dto = self.create_project(user_id, project_data)

        except InvalidWorkFlow:
            presenter.raise_invalid_workflow_id_exception()

        response = presenter.get_project_details_response(
            project_details_dto)

        return response

    def create_project(self, user_id: int, project_data: Dict):

        workflow_id = project_data['workflow_id']
        is_workflow_invalid = not self.storage.validate_workflow_id(
            workflow_id=workflow_id)

        if is_workflow_invalid:
            raise InvalidWorkFlow()

        project_dto = self._convert_project_data_to_dto(project_data)

        project_details_dto = self.storage.create_project(
            user_id=user_id,
            project_dto=project_dto
            )
        return project_details_dto

    @staticmethod
    def _convert_project_data_to_dto(project_data):

        project_dto = ProjectDto(
            name=project_data.get('name'),
            description=project_data.get('description'),
            workflow_id=project_data.get('workflow_id'),
            project_type=project_data.get('project_type'),
            developers=project_data.get('developers')
            )
        return project_dto
