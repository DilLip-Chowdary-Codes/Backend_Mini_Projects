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

class GetStatesForTaskInteractor:

    def __init__(self,
                 project_storage: ProjectStorageInterface,
                 task_storage: TaskStorageInterface,
                 project_presenter: ProjectPresenterInterface,
                 task_presenter: TaskPresenterInterface):

        self.project_storage = project_storage
        self.task_storage = task_storage
        self.project_presenter = project_presenter
        self.task_presenter = task_presenter

    def get_states_for_task_based_on_current_state(self, task_state_data):

        project_id = task_state_data['project_id']
        task_id = task_state_data['task_id']
        user_id = task_state_data['user_id']

        is_user_unauthorized = not self.project_storage\
            .validate_developer_for_project(
                user_id,
                project_id)

        if is_user_unauthorized:
            self.project_presenter.raise_unauthorized_developer_exception()


        is_project_id_invalid = not self.project_storage.validate_project_id(
            project_id=project_id)

        if is_project_id_invalid:
            self.project_presenter.raise_invalid_project_id_exception()

        task_dto = self.task_storage.validate_task_id(
            task_id=task_id)

        is_task_id_invalid = not task_dto

        if is_task_id_invalid:
            self.task_presenter.raise_invalid_task_id_exception()

        current_state_id = task_dto.state_id

        states_details_dtos = self.task_storage\
            .get_states_for_task_based_on_current_state(
                task_id=task_id,
                current_state_id=current_state_id
                )

        get_states_response = self.task_presenter.get_task_states_response(
            states_details_dtos)

        return get_states_response
