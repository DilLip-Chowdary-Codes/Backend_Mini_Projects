from typing import Dict
from project_management_portal.interactors.storages.project_storage_interface\
    import ProjectStorageInterface
from project_management_portal.interactors.presenters\
    .project_presenter_interface import ProjectPresenterInterface
from project_management_portal.dtos import ProjectDto

class CreateProjectInteractor:
    def __init__(self,
                 storage: ProjectStorageInterface,
                 presenter: ProjectPresenterInterface
                ):
        self.storage = storage
        self.presenter = presenter

    def create_project(self, user_id: int, project_data: Dict):

        is_developers_empty = project_data['developers'] is None
        if is_developers_empty:
            project_data['developers'] = []

        workflow_id = project_data['workflow_id']
        is_workflow_invalid = not self.storage.validate_workflow_id(
            workflow_id=workflow_id)

        if is_workflow_invalid:
            self.presenter.raise_invalid_workflow_id_exception()

        project_dto = self._convert_project_data_to_dto(project_data)

        project_details_dto = self.storage.create_project(
            user_id=user_id,
            project_dto=project_dto
            )
        response = self.presenter.get_project_details_response(
            project_details_dto)

        return response

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
