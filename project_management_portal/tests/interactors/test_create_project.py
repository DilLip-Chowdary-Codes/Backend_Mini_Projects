import pytest
from unittest.mock import create_autospec, Mock

from project_management_portal.interactors.storages.project_storage_interface\
    import ProjectStorageInterface
from project_management_portal.interactors.presenters\
    .project_presenter_interface import ProjectPresenterInterface
from project_management_portal.interactors.create_project_interactor\
    import CreateProjectInteractor

from .raw_inputs import project_data, project_dto
from .expected_responses import\
    create_project_response, project_details_dto
from project_management_portal.exceptions import InvalidWorkFlow

from django_swagger_utils.drf_server.exceptions\
    import NotFound, Unauthorized

from project_management_portal.constants.exception_messages\
    import INVALID_WORKFLOW

@pytest.mark.django_db
class TestCreateProject:
    def test_create_project_with_valid_values(self):

        #arrange
        user_id = 1
        storage = create_autospec(ProjectStorageInterface)
        presenter = create_autospec(ProjectPresenterInterface)
        interactor = CreateProjectInteractor(
            storage=storage,
            presenter=presenter)

        storage.validate_workflow_id.return_value = True
        storage.create_project.return_value = project_details_dto
        presenter.get_project_details_response\
            .return_value = create_project_response

        #act

        response = interactor.create_project(
            user_id=user_id,
            project_data=project_data
            )

        #assert
        assert response == create_project_response
        storage.validate_workflow_id.assert_called_once_with(
            workflow_id=project_data['workflow_id'])
        storage.create_project.assert_called_once_with(
            user_id=user_id,
            project_dto=project_dto)
        presenter.get_project_details_response.assert_called_once_with(
            project_details_dto=project_details_dto)

    def test_create_project_with_invalid_workflow(self):

        #arrange
        user_id = 1
        workflow_id = project_data.get('workflow_id')
        storage = create_autospec(ProjectStorageInterface)
        presenter = create_autospec(ProjectPresenterInterface)
        interactor = CreateProjectInteractor(
            storage=storage,
            presenter=presenter)

        storage.validate_workflow_id.return_value = False
        presenter.raise_invalid_workflow_id_exception.side_effect = \
            NotFound(*INVALID_WORKFLOW)
        expected_err_message = \
            "Invalid workflow, try with valid workflow"

        #act

        with pytest.raises(NotFound) as error:
            interactor.create_project(
                user_id=user_id,
                project_data=project_data
                )

        #assert

        storage.validate_workflow_id.assert_called_once_with(
            workflow_id=workflow_id)
        presenter.raise_invalid_workflow_id_exception.assert_called_once()
        assert str(error.value) == expected_err_message
