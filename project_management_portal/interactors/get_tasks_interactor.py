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

class GetTasksInteractor:

    def __init__(self,
                 project_storage: ProjectStorageInterface,
                 task_storage: TaskStorageInterface,
                 project_presenter: ProjectPresenterInterface,
                 task_presenter: TaskPresenterInterface):

        self.project_storage = project_storage
        self.task_storage = task_storage
        self.project_presenter = project_presenter
        self.task_presenter = task_presenter

    def get_tasks(self, user_id: int, project_id: int):
        is_project_invalid  = not self.project_storage.validate_project_id(
            project_id=project_id)

        if is_project_invalid:
            self.project_presenter.raise_invalid_project_id_exception()

        is_user_unauthorized = not self.project_storage\
            .validate_developer_for_project(user_id, project_id)

        if is_user_unauthorized:
            self.project_presenter.raise_unauthorized_developer_exception()

        tasks_details_dtos = self.task_storage.get_tasks(project_id)

        response = self.task_presenter.get_tasks_response(tasks_details_dtos)
        return response
