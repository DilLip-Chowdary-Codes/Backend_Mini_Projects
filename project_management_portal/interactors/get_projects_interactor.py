from project_management_portal.interactors.storages.project_storage_interface\
    import ProjectStorageInterface
from project_management_portal.interactors.presenters\
    .project_presenter_interface import ProjectPresenterInterface

class GetProjectsInteractor:
    def __init__(self,
                 project_storage: ProjectStorageInterface,
                 project_presenter: ProjectPresenterInterface
                ):
        self.project_storage = project_storage
        self.project_presenter = project_presenter

    def get_projects(self, user_id: int, offset: int, limit: int):

        if limit is None:
            limit = 100
        if offset is None:
            offset = 0

        is_admin = self.project_storage.validate_admin_scope(
            user_id=user_id)

        is_limit_value_invalid = not limit
        if is_limit_value_invalid:
            self.project_presenter.raise_invalid_limit_value_exception()

        is_offset_value_invalid = offset < 0
        if is_offset_value_invalid:
            self.project_presenter.raise_invalid_offset_value_exception()

        if is_admin:
            total_projects_count = self.project_storage\
                .get_admin_projects_count(user_id)
            all_project_dtos = self\
                .project_storage.get_projects_for_admin(
                    user_id=user_id,
                    offset=offset,
                    limit=limit)
        else:
            total_projects_count = self.project_storage\
                .get_user_projects_count(user_id)
            all_project_dtos = self\
                .project_storage.get_projects_for_user(
                    user_id=user_id,
                    offset=offset,
                    limit=limit)

        response = self.project_presenter.get_projects_response(
            total_projects_count=total_projects_count,
            all_projects_details_dtos=all_project_dtos
            )

        return response
