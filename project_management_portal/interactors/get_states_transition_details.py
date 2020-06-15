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

from project_management_portal.dtos import GetTransitionDetailsDto

class GetStatesTransitionDetailsInteractor:

    def __init__(self,
                 project_storage: ProjectStorageInterface,
                 task_storage: TaskStorageInterface,
                 project_presenter: ProjectPresenterInterface,
                 task_presenter: TaskPresenterInterface):

        self.project_storage = project_storage
        self.task_storage = task_storage
        self.project_presenter = project_presenter
        self.task_presenter = task_presenter

    def get_states_transition_details(self, transition_details_query_dict):

        project_id = transition_details_query_dict['project_id']
        task_id = transition_details_query_dict['task_id']

        project_dto = self.project_storage.validate_project_id(
            project_id)

        is_project_invalid = not project_dto

        if is_project_invalid:
            self.project_presenter.raise_invalid_project_id_exception()

        task_dto = self.task_storage.validate_task_id(task_id)
        is_task_invalid = not task_dto

        if is_task_invalid:
            self.task_presenter.raise_invalid_task_id_exception()

        workflow_id = project_dto.workflow_id
        from_state_id = task_dto.state_id
        to_state_id = transition_details_query_dict['to_state_id']

        is_transition_invalid = not self.project_storage\
            .validate_state_transition(
                workflow_id,
                from_state_id,
                to_state_id)

        if is_transition_invalid:
            self.project_presenter.raise_invalid_transition_exception()

        get_transition_details_query_dto = self\
            ._convert_get_transition_query_data_to_dto(
                transition_details_query_dict, from_state_id)

        transition_details_dtos = self.project_storage\
            .get_states_transition_details(
                get_transition_details_query_dto)

        transition_details_response = self.project_presenter\
            .get_transition_details_response(transition_details_dtos)

        return transition_details_response

    @staticmethod
    def _convert_get_transition_query_data_to_dto(
            transition_details_query_dict,
            from_state_id) -> GetTransitionDetailsDto:

        get_transition_details_dto = GetTransitionDetailsDto(
            project_id=transition_details_query_dict['project_id'],
            task_id=transition_details_query_dict['task_id'],
            from_state_id=from_state_id,
            to_state_id=transition_details_query_dict['to_state_id']
            )

        return get_transition_details_dto
