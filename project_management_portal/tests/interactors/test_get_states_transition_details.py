from unittest.mock import create_autospec, Mock
import pytest

from django_swagger_utils.drf_server.exceptions\
    import NotFound

from project_management_portal.interactors.get_states_transition_details\
    import GetStatesTransitionDetailsInteractor

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
from project_management_portal.constants.exception_messages\
    import INVALID_PROJECT, INVALID_TASK, INVALID_TRANSITION

class TestGetStatesTransitionDetails:

    def test_get_states_transition_details(self):

        #arrange
        from .raw_inputs\
            import task_dto, project_dto,\
                   transition_details_query_dict

        from .expected_responses\
            import transitions_details_dtos,\
                   transition_details_response,\
                   get_transition_details_dto

        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = GetStatesTransitionDetailsInteractor(
            task_storage=task_storage,
            project_storage=project_storage,
            task_presenter=task_presenter,
            project_presenter=project_presenter)

        project_id = transition_details_query_dict['project_id']
        task_id = transition_details_query_dict['task_id']
        workflow_id = project_dto.workflow_id
        from_state_id = task_dto.state_id
        to_state_id = transition_details_query_dict['to_state_id']

        project_storage.validate_project_id.return_value = project_dto
        task_storage.validate_task_id.return_value = task_dto
        project_storage.validate_state_transition.return_value = True
        project_storage.get_states_transition_details\
            .return_value = transitions_details_dtos
        project_presenter.get_transition_details_response\
            .return_value = transition_details_response

        #act
        response = interactor.get_states_transition_details(
            transition_details_query_dict)

        #assert
        assert response == transition_details_response
        project_storage.validate_project_id.assert_called_once_with(
            project_id)
        task_storage.validate_task_id.assert_called_once_with(
            task_id)
        project_storage.validate_state_transition.assert_called_once_with(
            workflow_id,
            from_state_id,
            to_state_id)
        project_storage.get_states_transition_details.assert_called_once_with(
            get_transition_details_dto)
        project_presenter.get_transition_details_response\
            .assert_called_once_with(transitions_details_dtos)

    def test_get_states_transition_details_invalid_project_id(self):

        #arrange
        from .raw_inputs\
            import transition_details_query_dict

        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = GetStatesTransitionDetailsInteractor(
            task_storage=task_storage,
            project_storage=project_storage,
            task_presenter=task_presenter,
            project_presenter=project_presenter)

        project_storage.validate_project_id.return_value = None
        project_presenter.raise_invalid_project_id_exception\
            .side_effect = NotFound(*INVALID_PROJECT)
        expected_error_msg = "Invalid project_id, try with valid project_id"

        #act
        with pytest.raises(NotFound) as error:
            interactor.get_states_transition_details(
                transition_details_query_dict)

        #assert
        assert error.value.message == expected_error_msg
        project_storage.validate_project_id.assert_called_once_with(
            transition_details_query_dict['project_id'])
        project_presenter.raise_invalid_project_id_exception\
            .assert_called_once()

    def test_get_states_transition_details_invalid_task_id(self):

        #arrange
        from .raw_inputs\
            import project_dto, transition_details_query_dict

        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = GetStatesTransitionDetailsInteractor(
            task_storage=task_storage,
            project_storage=project_storage,
            task_presenter=task_presenter,
            project_presenter=project_presenter)

        project_storage.validate_project_id.return_value = project_dto
        task_storage.validate_task_id.return_value = None
        task_presenter.raise_invalid_task_id_exception\
            .side_effect = NotFound(*INVALID_TASK)
        expected_error_msg = "Invalid Task, try with valid task"

        #act
        with pytest.raises(NotFound) as error:
            interactor.get_states_transition_details(
                transition_details_query_dict)

        #assert
        assert error.value.message == expected_error_msg
        project_storage.validate_project_id.assert_called_once_with(
            transition_details_query_dict['project_id'])
        task_storage.validate_task_id.assert_called_once_with(
            transition_details_query_dict['task_id'])
        task_presenter.raise_invalid_task_id_exception\
            .assert_called_once()

    def test_get_states_transition_details_invalid_state_transition(self):

        #arrange
        from .raw_inputs\
            import project_dto, task_dto, transition_details_query_dict

        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = GetStatesTransitionDetailsInteractor(
            task_storage=task_storage,
            project_storage=project_storage,
            task_presenter=task_presenter,
            project_presenter=project_presenter)

        project_storage.validate_project_id.return_value = project_dto
        task_storage.validate_task_id.return_value = task_dto
        project_storage\
            .validate_state_transition\
            .return_value = False
        project_presenter\
            .raise_invalid_transition_exception\
            .side_effect = NotFound(*INVALID_TRANSITION)

        expected_error_msg = "Invalid Transition, try with valid transition"

        #act
        with pytest.raises(NotFound) as error:
            interactor.get_states_transition_details(
                transition_details_query_dict)

        #assert
        assert error.value.message == expected_error_msg
        project_storage.validate_project_id.assert_called_once_with(
            transition_details_query_dict['project_id'])
        task_storage.validate_task_id.assert_called_once_with(
            transition_details_query_dict['task_id'])
        project_storage\
            .validate_state_transition.assert_called_once_with(
                project_dto.workflow_id,
                task_dto.state_id,
                transition_details_query_dict['to_state_id'])
        project_presenter.raise_invalid_transition_exception\
            .assert_called_once()
