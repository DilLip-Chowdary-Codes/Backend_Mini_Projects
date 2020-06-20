from unittest.mock import create_autospec

import pytest
#interactor
from project_management_portal.interactors.create_task_interactor\
    import CreateTaskInteractor
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
    import NotFound, Unauthorized

from project_management_portal.constants.exception_messages\
    import INVALID_PROJECT, INVALID_STATE, UN_AUTHORIZED_DEVELOPER

from .raw_inputs import task_data, task_dto, task_details_dto
from .expected_responses import task_details_response

class TestCreateTask:

    def test_create_task_with_valid_values(self):

        #arrange
        user_id = 1
        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = CreateTaskInteractor(
            task_storage=task_storage,
            project_storage=project_storage
            )

        project_storage.validate_project_id.return_value = True
        task_storage.validate_state_id.return_value = True
        project_storage.validate_developer_for_project.return_value = True
        task_storage.create_task.return_value = task_details_dto
        task_presenter.get_create_task_response.return_value = task_details_response

        #act
        response = interactor.create_task_wrapper(
            user_id=user_id,
            task_data=task_data,
            project_presenter=project_presenter,
            task_presenter=task_presenter)

        #assert
        assert response == task_details_response
        project_storage.validate_project_id.assert_called_once_with(
            project_id=task_data.get('project_id'))
        task_storage.validate_state_id.assert_called_once_with(
            state_id=task_data.get('state_id'))
        project_storage\
            .validate_developer_for_project.assert_called_once_with(
                user_id, task_dto.project_id)
        task_storage.create_task.assert_called_once_with(
            user_id=user_id,
            task_dto=task_dto)
        task_presenter.get_create_task_response.assert_called_once_with(
            task_details_dto=task_details_dto)

    def test_create_task_with_invalid_project_id(self):

        #arrange
        user_id = 1
        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = CreateTaskInteractor(
            task_storage=task_storage,
            project_storage=project_storage
            )

        project_storage.validate_project_id.return_value = False
        project_presenter.raise_invalid_project_id_exception\
            .side_effect = NotFound(*INVALID_PROJECT)
        expected_error_msg = "Invalid project_id, try with valid project_id"

        #act
        with pytest.raises(NotFound) as error:
            interactor.create_task_wrapper(
            user_id=user_id,
            task_data=task_data,
            project_presenter=project_presenter,
            task_presenter=task_presenter
            )

        #assert
        assert str(error.value) == expected_error_msg
        project_storage.validate_project_id.assert_called_once_with(
            project_id=task_data.get('project_id'))
        project_presenter.raise_invalid_project_id_exception.assert_called_once()

    def test_create_task_with_invalid_state_id(self):

        #arrange
        user_id = 1
        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = CreateTaskInteractor(
            task_storage=task_storage,
            project_storage=project_storage
            )

        project_storage.validate_project_id.return_value = True
        task_storage.validate_state_id.return_value = False
        task_presenter.raise_invalid_state_id_exception\
            .side_effect = NotFound(*INVALID_STATE)
        expected_error_msg = "Invalid state_id, try with valid state_id"

        #act
        with pytest.raises(NotFound) as error:
            interactor.create_task_wrapper(
            user_id=user_id,
            task_data=task_data,
            project_presenter=project_presenter,
            task_presenter=task_presenter
            )

        #assert
        assert str(error.value) == expected_error_msg
        project_storage.validate_project_id.assert_called_once_with(
            project_id=task_data.get('project_id'))
        task_storage.validate_state_id.assert_called_once_with(
            state_id=task_data.get('state_id'))
        task_presenter.raise_invalid_state_id_exception.assert_called_once()

    def test_create_task_with_unauthorized_user(self):

        #arrange
        user_id = 1
        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = CreateTaskInteractor(
            task_storage=task_storage,
            project_storage=project_storage
            )

        project_storage.validate_project_id.return_value = True
        task_storage.validate_state_id.return_value = True
        project_storage.validate_developer_for_project.return_value = False
        project_presenter.raise_unauthorized_developer_exception\
            .side_effect = Unauthorized(*UN_AUTHORIZED_DEVELOPER)
        expected_error_msg = "Developer not allowed to access this resource"

        #act
        with pytest.raises(Unauthorized) as error:
            interactor.create_task_wrapper(
                user_id=user_id,
                task_data=task_data,
            project_presenter=project_presenter,
            task_presenter=task_presenter
            )

        #assert
        assert str(error.value) == expected_error_msg
        project_storage.validate_project_id.assert_called_once_with(
            project_id=task_data.get('project_id'))
        task_storage.validate_state_id.assert_called_once_with(
            state_id=task_data.get('state_id'))
        project_storage\
            .validate_developer_for_project\
                .assert_called_once_with(user_id, task_dto.project_id)
        project_presenter.raise_unauthorized_developer_exception\
            .assert_called_once()
