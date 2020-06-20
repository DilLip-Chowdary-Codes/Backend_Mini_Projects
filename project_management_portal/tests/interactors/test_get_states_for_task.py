import pytest
from unittest.mock import create_autospec, Mock

from project_management_portal.interactors.get_states_for_task_interactor\
    import GetStatesForTaskInteractor

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

class TestGetStatesForTaskBasesOnCurrentState:

    def test_get_states_for_task_with_valid_values(self):

        #arrange
        from .raw_inputs import project_dto, task_dto, task_state_data
        from .expected_responses\
            import available_states_dtos, get_states_response

        project_id = task_state_data['project_id']
        user_id = task_state_data['user_id']
        task_id = task_state_data['task_id']
        current_state_id = task_dto.state_id
        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = GetStatesForTaskInteractor(
            task_storage=task_storage,
            project_storage=project_storage)
        project_storage\
            .validate_developer_for_project.return_value = True
        project_storage.validate_project_id.return_value = project_dto
        task_storage.validate_task_id.return_value = task_dto
        task_storage\
            .get_states_for_task_based_on_current_state\
                .return_value = available_states_dtos
        task_presenter.get_task_states_response\
            .return_value = get_states_response

        #act
        response = interactor.get_states_for_task_based_on_current_state_wrapper(
            task_state_data,
            project_presenter=project_presenter,
            task_presenter=task_presenter)

        #assert
        assert response == get_states_response
        project_storage\
            .validate_developer_for_project.assert_called_once_with(
                user_id,
                project_id)
        project_storage.validate_project_id.assert_called_once_with(
            project_id)
        task_storage.validate_task_id.assert_called_once_with(
            task_id)
        task_storage\
            .get_states_for_task_based_on_current_state\
                .assert_called_once_with(
                    task_id, current_state_id)
        task_presenter.get_task_states_response.assert_called_once_with(
            available_states_dtos)

    def test_get_states_for_task_with_unauthorized_developer(self):

        #arrange
        from .raw_inputs import task_state_data
        from django_swagger_utils.drf_server.exceptions\
            import NotFound

        from project_management_portal.constants.exception_messages\
            import UN_AUTHORIZED_DEVELOPER

        project_id = task_state_data['project_id']
        user_id = task_state_data['user_id']
        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = GetStatesForTaskInteractor(
            task_storage=task_storage,
            project_storage=project_storage
            )
        project_storage\
            .validate_developer_for_project.return_value = False
        project_presenter.raise_unauthorized_developer_exception\
            .side_effect = NotFound(*UN_AUTHORIZED_DEVELOPER)
        expected_error_msg = "Developer not allowed to access this resource"

        #act
        with pytest.raises(NotFound) as error:
            interactor.get_states_for_task_based_on_current_state_wrapper(
            task_state_data,
            project_presenter=project_presenter,
            task_presenter=task_presenter)

        #assert
        assert str(error.value) == expected_error_msg
        project_storage\
            .validate_developer_for_project.assert_called_once_with(
                user_id,
                project_id)
        project_presenter.raise_unauthorized_developer_exception\
            .assert_called_once()

    def test_get_states_for_task_with_invalid_project_id(self):

        #arrange
        from .raw_inputs import task_state_data
        from django_swagger_utils.drf_server.exceptions\
            import NotFound

        from project_management_portal.constants.exception_messages\
            import INVALID_PROJECT

        project_id = task_state_data['project_id']
        user_id = task_state_data['user_id']
        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = GetStatesForTaskInteractor(
            task_storage=task_storage,
            project_storage=project_storage
            )
        project_storage\
            .validate_developer_for_project.return_value = True
        project_storage.validate_project_id.return_value = None
        project_presenter.raise_invalid_project_id_exception\
            .side_effect = NotFound(*INVALID_PROJECT)
        expected_error_msg = "Invalid project_id, try with valid project_id"

        #act
        with pytest.raises(NotFound) as error:
            interactor.get_states_for_task_based_on_current_state_wrapper(
                task_state_data,
                project_presenter=project_presenter,
                task_presenter=task_presenter)

        #assert
        assert str(error.value) == expected_error_msg
        project_storage\
            .validate_developer_for_project.assert_called_once_with(
                user_id,
                project_id)
        project_storage.validate_project_id.assert_called_once_with(
            project_id)
        project_presenter.raise_invalid_project_id_exception\
            .assert_called_once()

    def test_get_states_for_task_with_(self):

        #arrange
        from .raw_inputs import project_dto, task_state_data
        from django_swagger_utils.drf_server.exceptions\
            import NotFound

        from project_management_portal.constants.exception_messages\
            import INVALID_TASK

        project_id = task_state_data['project_id']
        user_id = task_state_data['user_id']
        task_id = task_state_data['task_id']
        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = GetStatesForTaskInteractor(
            task_storage=task_storage,
            project_storage=project_storage
            )
        project_storage\
            .validate_developer_for_project.return_value = True
        project_storage.validate_project_id.return_value = project_dto
        task_storage.validate_task_id.return_value = None
        task_presenter.raise_invalid_task_id_exception\
            .side_effect = NotFound(*INVALID_TASK)
        expected_error_msg = "Invalid Task, try with valid task"

        #act
        with pytest.raises(NotFound) as error:
            interactor.get_states_for_task_based_on_current_state_wrapper(
                task_state_data,
                project_presenter=project_presenter,
                task_presenter=task_presenter)

        #assert
        assert str(error.value) == expected_error_msg
        project_storage\
            .validate_developer_for_project.assert_called_once_with(
                user_id,
                project_id)
        project_storage.validate_project_id.assert_called_once_with(
            project_id)
        task_storage.validate_task_id.assert_called_once_with(
            task_id)
        task_presenter.raise_invalid_task_id_exception.assert_called_once()
