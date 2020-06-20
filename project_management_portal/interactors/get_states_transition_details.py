from project_management_portal\
    .interactors.storages.task_storage_interface\
    import TaskStorageInterface
from project_management_portal\
    .interactors.storages.project_storage_interface\
    import ProjectStorageInterface
from project_management_portal\
    .interactors.presenters.project_presenter_interface\
    import ProjectPresenterInterface
from project_management_portal\
    .interactors.presenters.task_presenter_interface\
    import TaskPresenterInterface
from project_management_portal.dtos import GetTransitionDetailsDto
from project_management_portal.exceptions\
    import InvalidProjectId, InvalidTaskId, InvalidTransition

class GetStatesTransitionDetailsInteractor:

    def __init__(self,
                 project_storage: ProjectStorageInterface,
                 task_storage: TaskStorageInterface):

        self.project_storage = project_storage
        self.task_storage = task_storage

    def get_states_transition_details_wrapper(
            self,
            transition_details_query_dict,
            project_presenter: ProjectPresenterInterface,
            task_presenter: TaskPresenterInterface):

        try:
            transition_details_dtos = self.get_states_transition_details(
                transition_details_query_dict)

        except InvalidProjectId:
            project_presenter.raise_invalid_project_id_exception()
        except InvalidTaskId:
            task_presenter.raise_invalid_task_id_exception()
        except InvalidTransition:
            project_presenter.raise_invalid_transition_exception()

        transition_details_response = project_presenter\
            .get_transition_details_response(transition_details_dtos)

        return transition_details_response

    def get_states_transition_details(self, transition_details_query_dict):

        project_id = transition_details_query_dict['project_id']
        task_id = transition_details_query_dict['task_id']

        project_dto = self.project_storage.validate_project_id(
            project_id)

        is_project_invalid = not project_dto

        if is_project_invalid:
            raise InvalidProjectId()

        task_dto = self.task_storage.validate_task_id(task_id)
        is_task_invalid = not task_dto

        if is_task_invalid:
            raise InvalidTaskId()

        workflow_id = project_dto.workflow_id
        from_state_id = task_dto.state_id
        to_state_id = transition_details_query_dict['to_state_id']

        is_transition_invalid = not self.project_storage\
            .validate_state_transition(
                workflow_id,
                from_state_id,
                to_state_id)

        if is_transition_invalid:
            raise InvalidTransition()

        get_transition_details_query_dto = self\
            ._convert_get_transition_query_data_to_dto(
                transition_details_query_dict, from_state_id)

        transition_details_dtos = self.project_storage\
            .get_states_transition_details(
                get_transition_details_query_dto)

        return transition_details_dtos

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
