from project_management_portal.interactors.storages.project_storage_interface\
    import ProjectStorageInterface
from project_management_portal.interactors.presenters\
    .project_presenter_interface import ProjectPresenterInterface
from project_management_portal.exceptions\
    import InvalidLimitValue, InvalidOffsetValue
from project_management_portal.interactors.mixins.validations\
    import ValidationsMixin
from project_management_portal.constants import DEFAULT_LIMIT, DEFAULT_OFFSET
from project_management_portal.adapters.service_adapter\
    import get_service_adapter

class GetProjectsInteractor(ValidationsMixin):
    def __init__(self,
                 project_storage: ProjectStorageInterface
                ):
        self.project_storage = project_storage

    def get_projects_wrapper(self,  user_id: int, offset: int, limit: int,
                             project_presenter: ProjectPresenterInterface):
        try:
            total_projects_count, all_project_dtos = \
                self.get_projects(user_id, offset, limit)

        except InvalidLimitValue:
            project_presenter.raise_invalid_limit_value_exception()
        except InvalidOffsetValue:
            project_presenter.raise_invalid_offset_value_exception()

        response = project_presenter.get_projects_response(
            total_projects_count=total_projects_count,
            all_projects_details_dtos=all_project_dtos
            )

        return response


    def get_projects(self, user_id: int, offset: int, limit: int):

        self.validate_limit(limit)
        self.validate_offset(offset)

        if limit is None:
            limit = DEFAULT_LIMIT
        if offset is None:
            offset = DEFAULT_OFFSET
        
        adapter_service = get_service_adapter()
        user_service = adapter_service.user_service

        is_admin = user_service.is_user_admin(user_id=user_id)

        if is_admin:
            total_projects_count = self.project_storage\
                .get_admin_projects_count(user_id)
            all_project_dtos = self\
                .project_storage.get_projects_for_admin(user_id=user_id,
                                                        offset=offset,
                                                        limit=limit)
        else:
            total_projects_count = self.project_storage\
                .get_user_projects_count(user_id)
            all_project_dtos = self\
                .project_storage.get_projects_for_user(user_id=user_id,
                                                       offset=offset,
                                                       limit=limit)
        return total_projects_count, all_project_dtos
