from unittest.mock import create_autospec, Mock
import pytest

#interactor
from project_management_portal.interactors.task_state_transition_interactor\
    import TaskStateTransitionInteractor
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

from django_swagger_utils.drf_server.exceptions\
    import NotFound, BadRequest

class TestTaskTransition:

    def test_update_task_state(self):

        #arrange
        from .raw_inputs\
            import task_dto, project_dto,\
                   update_task_state_input_data,\
                   update_task_state_query_dto

        from .expected_responses\
            import updated_task_details_response,\
                   updated_task_details_dto,\
                   mandatory_checklist_dtos

        project_id = update_task_state_input_data.get('project_id')
        task_id = update_task_state_input_data['task_id']
        to_state_id = update_task_state_input_data['to_state_id']

        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = TaskStateTransitionInteractor(
            task_storage=task_storage,
            project_storage=project_storage)

        project_storage.validate_project_id.return_value = project_dto
        task_storage.validate_task_id.return_value = task_dto
        project_storage.validate_state_transition.return_value = True
        project_storage.get_transition_mandatory_checklist\
            .return_value = mandatory_checklist_dtos
        task_storage.update_task_state.return_value\
            = updated_task_details_dto
        task_presenter.get_task_details_response.return_value\
            = updated_task_details_response

        #act
        response = interactor.update_task_state_wrapper(
            update_task_state_input_data,
            project_presenter,
            task_presenter)

        #assert
        assert response == updated_task_details_response
        project_storage.validate_project_id.assert_called_once_with(
            project_id=project_id)
        task_storage.validate_task_id.assert_called_once_with(
            task_id=task_id)
        project_storage.validate_state_transition.assert_called_once_with(
            project_dto.workflow_id,
            task_dto.state_id,
            to_state_id
            )
        project_storage.get_transition_mandatory_checklist\
            .assert_called_once_with(update_task_state_query_dto)
        task_presenter.get_task_details_response.assert_called_once_with(
            updated_task_details_dto)

    def test_update_task_state_invalid_project(self):

        #arrange
        from .raw_inputs import update_task_state_input_data
        from project_management_portal.constants.exception_messages\
            import INVALID_PROJECT

        project_id = update_task_state_input_data.get('project_id')
        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = TaskStateTransitionInteractor(
            task_storage=task_storage,
            project_storage=project_storage)

        project_storage.validate_project_id.return_value = False
        project_presenter.raise_invalid_project_id_exception\
            .side_effect = NotFound(*INVALID_PROJECT)
        expected_error_message\
            = "Invalid project_id, try with valid project_id"

        #act
        with pytest.raises(NotFound) as error:
            interactor.update_task_state_wrapper(update_task_state_input_data,
                                                 project_presenter,
                                                 task_presenter)

        #assert
        assert error.value.message == expected_error_message
        project_storage.validate_project_id.assert_called_once_with(
            project_id=project_id)
        project_presenter.raise_invalid_project_id_exception\
            .assert_called_once()

    def test_update_task_state_invalid_task(self):

        #arrange
        from .raw_inputs import project_dto, update_task_state_input_data
        from project_management_portal.constants.exception_messages\
            import INVALID_TASK

        project_id = update_task_state_input_data.get('project_id')
        task_id = update_task_state_input_data['task_id']
        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = TaskStateTransitionInteractor(
            task_storage=task_storage,
            project_storage=project_storage)

        project_storage.validate_project_id.return_value = project_dto
        task_storage.validate_task_id.return_value = False
        task_presenter.raise_invalid_task_id_exception\
            .side_effect = NotFound(*INVALID_TASK)
        expected_err_message = "Invalid Task, try with valid task"

        #act
        with pytest.raises(NotFound) as error:
            interactor.update_task_state_wrapper(update_task_state_input_data,
                                                 project_presenter,
                                                 task_presenter)

        #assert
        assert error.value.message == expected_err_message
        project_storage.validate_project_id.assert_called_once_with(
            project_id=project_id)
        task_storage.validate_task_id.assert_called_once_with(
            task_id=task_id)
        task_presenter.raise_invalid_task_id_exception.assert_called_once()

    def test_update_task_state_invalid_transition(self):

        #arrange
        from .raw_inputs import task_dto, project_dto, update_task_state_input_data
        from project_management_portal.constants.exception_messages\
            import INVALID_TRANSITION

        project_id = update_task_state_input_data.get('project_id')
        task_id = update_task_state_input_data['task_id']
        to_state_id = update_task_state_input_data['to_state_id']
        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = TaskStateTransitionInteractor(
            task_storage=task_storage,
            project_storage=project_storage)

        project_storage.validate_project_id.return_value = project_dto
        task_storage.validate_task_id.return_value = task_dto
        project_storage.validate_state_transition.return_value = False
        project_presenter.raise_invalid_transition_exception\
            .side_effect = NotFound(*INVALID_TRANSITION)
        expected_error_message\
            = "Invalid Transition, try with valid transition"

        #act
        with pytest.raises(NotFound) as error:
            interactor.update_task_state_wrapper(update_task_state_input_data,
                                                 project_presenter,
                                                 task_presenter)

        #assert
        assert error.value.message == expected_error_message
        project_storage.validate_project_id.assert_called_once_with(
            project_id=project_id)
        task_storage.validate_task_id.assert_called_once_with(
            task_id=task_id)
        project_storage.validate_state_transition.assert_called_once_with(
            project_dto.workflow_id,
            task_dto.state_id,
            to_state_id
            )
        project_presenter.raise_invalid_transition_exception\
            .assert_called_once()


    def test_update_task_state_with_unchecked_mandatory_checkist(self):

        #arrange
        from .raw_inputs import task_dto,\
        project_dto,\
        update_task_state_input_data_with_unchecked_mandatory_checklist,\
        update_task_state_query_dto_with_unchecked_mandatory_checklist

        from .expected_responses import mandatory_checklist_dtos

        from project_management_portal.constants.exception_messages\
            import CHECKLIST_NOT_SATISFIED
        update_task_state_input_data\
            = update_task_state_input_data_with_unchecked_mandatory_checklist
        project_id = update_task_state_input_data.get('project_id')
        task_id = update_task_state_input_data['task_id']
        to_state_id = update_task_state_input_data['to_state_id']
        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = TaskStateTransitionInteractor(
            task_storage=task_storage,
            project_storage=project_storage)

        project_storage.validate_project_id.return_value = project_dto
        task_storage.validate_task_id.return_value = task_dto
        project_storage.validate_state_transition.return_value = True
        project_storage.get_transition_mandatory_checklist\
            .return_value = mandatory_checklist_dtos
        project_presenter.raise_checklist_not_satisfied_exception\
            .side_effect = BadRequest(*CHECKLIST_NOT_SATISFIED)
        expected_error_message\
            = "Check list mandatory fields not checked"

        #act
        with pytest.raises(BadRequest) as error:
            interactor.update_task_state_wrapper(update_task_state_input_data,
                                                 project_presenter,
                                                 task_presenter)

        #assert
        assert error.value.message == expected_error_message
        project_storage.validate_project_id.assert_called_once_with(
            project_id=project_id)
        task_storage.validate_task_id.assert_called_once_with(
            task_id=task_id)
        project_storage.validate_state_transition.assert_called_once_with(
            project_dto.workflow_id,
            task_dto.state_id,
            to_state_id
            )
        project_storage.get_transition_mandatory_checklist\
            .assert_called_once_with(
                update_task_state_query_dto_with_unchecked_mandatory_checklist
                )
        project_presenter.raise_checklist_not_satisfied_exception\
            .assert_called_once()
