from typing import Dict
#storages
from project_management_portal\
    .interactors.storages.task_storage_interface\
    import TaskStorageInterface
from project_management_portal\
    .interactors.storages.project_storage_interface\
    import ProjectStorageInterface
#presenters
from project_management_portal\
    .interactors.presenters.project_presenter_interface\
    import ProjectPresenterInterface
from project_management_portal\
    .interactors.presenters.task_presenter_interface\
    import TaskPresenterInterface
from project_management_portal.dtos import TaskDto

class InvalidProjectId(Exception):
    pass

class InvalidStateId(Exception):
    pass

class UnauthorizedUser(Exception):
    pass

class CreateTaskInteractor:

    def __init__(self,
                 project_storage: ProjectStorageInterface,
                 task_storage: TaskStorageInterface):

        self.project_storage = project_storage
        self.task_storage = task_storage
    
    def create_task_wrapper(self, user_id: int, task_data: Dict,
                            project_presenter: ProjectPresenterInterface,
                            task_presenter: TaskPresenterInterface
                           ):

        try:
            task_details_dto = self.create_task(user_id, task_data)

        except InvalidProjectId:
            project_presenter.raise_invalid_project_id_exception()
        except InvalidStateId:
            task_presenter.raise_invalid_state_id_exception()
        except UnauthorizedUser:
            project_presenter.raise_unauthorized_developer_exception()
        else:
            create_task_response = task_presenter.get_create_task_response(
            task_details_dto=task_details_dto)

        return create_task_response

    def create_task(self, user_id: int, task_data: Dict):

        task_dto = self._convert_task_data_to_dto(task_data)

        is_project_invalid = not self.project_storage.validate_project_id(
            project_id=task_dto.project_id)

        if is_project_invalid:
            self._raise_invalid_project_id_exception()

        is_state_invalid = not self.task_storage.validate_state_id(
            state_id=task_dto.state_id)

        if is_state_invalid:
            self._raise_invalid_state_id_exception()

        project_id = task_dto.project_id
        is_user_unauthorized = not self.project_storage\
            .validate_developer_for_project(user_id, project_id)

        if is_user_unauthorized:
            self._raise_unauthorized_user_exception()

        task_details_dto = self.task_storage.create_task(
            user_id=user_id,
            task_dto=task_dto)

        return task_details_dto

    @staticmethod
    def _convert_task_data_to_dto(task_data: Dict):
        task_dto = TaskDto(
            project_id=task_data.get('project_id'),
            issue_type=task_data.get('issue_type'),
            title=task_data.get('title'),
            description=task_data.get('description'),
            state_id=task_data.get('state_id')
            )
        return task_dto
    
    @staticmethod
    def _raise_invalid_project_id_exception():
        raise InvalidProjectId()
    
    @staticmethod
    def _raise_invalid_state_id_exception():
        raise InvalidStateId()
    
    @staticmethod
    def _raise_unauthorized_user_exception():
        raise UnauthorizedUser()
