from unittest.mock import create_autospec

import pytest

from project_management_portal.interactors.get_tasks_interactor\
    import GetTasksInteractor

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

from django_swagger_utils.drf_server.exceptions\
    import NotFound, Unauthorized

from .raw_inputs import task_data, tasks_dtos, tasks_details_dtos
from .expected_responses import tasks_details_response

class TestGetTasks:

    def test_get_tasks_with_valid_values(self):

        #arrange
        project_id = 1
        user_id = 1
        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = GetTasksInteractor(
            task_storage=task_storage,
            project_storage=project_storage,
            task_presenter=task_presenter,
            project_presenter=project_presenter)

        project_storage.validate_project_id.return_value = True
        project_storage.validate_developer_for_project.return_value = True
        task_storage.get_tasks.return_value = tasks_details_dtos
        task_presenter.get_tasks_response.return_value\
            = tasks_details_response

        #act
        response = interactor.get_tasks(
            user_id=user_id,
            project_id=project_id)

        #assert
        assert response == tasks_details_response
        project_storage.validate_project_id.assert_called_once_with(
            project_id=project_id
            )
        project_storage.validate_developer_for_project(
            user_id=user_id,
            project_id=project_id)
        task_storage.get_tasks.assert_called_once_with(
            project_id=project_id)
        task_presenter.get_tasks_response.assert_called_once_with(
            tasks_details_dtos=tasks_details_dtos)

    def test_get_tasks_with_invalid_project(self):

        #arrange
        from project_management_portal.constants.exception_messages\
            import INVALID_PROJECT

        project_id = 1
        user_id = 1

        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = GetTasksInteractor(
            task_storage=task_storage,
            project_storage=project_storage,
            task_presenter=task_presenter,
            project_presenter=project_presenter)

        project_storage.validate_project_id.return_value = False
        task_storage.get_tasks.return_value = tasks_details_dtos
        project_presenter.raise_invalid_project_id_exception\
            .side_effect = NotFound(*INVALID_PROJECT)
        expection_error_msg = "Invalid project_id, try with valid project_id"
        
        #act
        with pytest.raises(NotFound) as error:
            interactor.get_tasks(
                user_id=user_id,
                project_id=project_id)

        #assert
        assert error.value.message == expection_error_msg
        project_storage.validate_project_id.assert_called_once_with(
            project_id=project_id
            )
        project_presenter.raise_invalid_project_id_exception\
            .assert_called_once()

    def test_get_tasks_with_unauthorized_user(self):

        #arrange
        from project_management_portal.constants.exception_messages\
            import UN_AUTHORIZED_DEVELOPER

        project_id = 1
        user_id = 1

        task_storage = create_autospec(TaskStorageInterface)
        project_storage = create_autospec(ProjectStorageInterface)
        task_presenter = create_autospec(TaskPresenterInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)

        interactor = GetTasksInteractor(
            task_storage=task_storage,
            project_storage=project_storage,
            task_presenter=task_presenter,
            project_presenter=project_presenter)

        project_storage.validate_project_id.return_value = True
        project_storage.validate_developer_for_project.return_value = False
        project_presenter.raise_unauthorized_developer_exception\
            .side_effect = Unauthorized(*UN_AUTHORIZED_DEVELOPER)
        expection_error_msg = "Developer not allowed to access this resource"

        #act
        with pytest.raises(Unauthorized) as error:
            interactor.get_tasks(
                user_id=user_id,
                project_id=project_id)

        #assert
        assert error.value.message == expection_error_msg
        project_storage.validate_project_id.assert_called_once_with(
            project_id=project_id
            )
        project_storage.validate_developer_for_project\
            .assert_called_once_with(
                user_id=user_id,
                project_id=project_id)
        project_presenter.raise_unauthorized_developer_exception\
            .assert_called_once()
