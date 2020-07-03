import pytest
from unittest.mock import create_autospec, Mock, patch
from django_swagger_utils.drf_server.exceptions\
    import NotFound, Unauthorized

from project_management_portal.adapters.user_service import UserService
from project_management_portal.interactors.storages.project_storage_interface\
    import ProjectStorageInterface
from project_management_portal.interactors.presenters\
    .project_presenter_interface import ProjectPresenterInterface
from project_management_portal.interactors.create_project_interactor\
    import CreateProjectInteractor
from project_management_portal.exceptions import InvalidWorkFlow
from project_management_portal.constants.exception_messages\
    import INVALID_WORKFLOW

from .raw_inputs import \
    project_data, project_dto, projects_details_dto_for_create_project,\
    user_dtos, create_project_request_dto


from .expected_responses import\
    create_project_response

@pytest.mark.django_db
class TestCreateProject:

    @patch.object(UserService, 'interface')
    def test_create_project_with_valid_values(self, interface_mock, snapshot):

        #arrange
        user_id = 1
        storage = create_autospec(ProjectStorageInterface)
        presenter = create_autospec(ProjectPresenterInterface)
        interactor = CreateProjectInteractor(storage=storage)
        projects_details_dto = projects_details_dto_for_create_project
        storage.validate_workflow_id.return_value = True
        storage.create_project.return_value = project_dto
        interface_mock.get_user_dtos.return_value = user_dtos
        presenter.get_project_details_response\
            .return_value = create_project_response

        #act
        project_details = interactor.create_project_wrapper(
            user_id=user_id,
            project_data=project_data,
            presenter=presenter
            )

        #assert
        snapshot.assert_match(project_details, 'project_data')
        storage.validate_workflow_id.assert_called_once_with(
            workflow_id=project_data['workflow_id'])
        storage.create_project.assert_called_once_with(
            user_id=user_id,
            project_dto=create_project_request_dto)

        presenter.get_project_details_response.assert_called_once_with(
            projects_details_dto=projects_details_dto)

    def test_create_project_with_invalid_workflow(self, snapshot):

        #arrange
        user_id = 1
        workflow_id = project_data.get('workflow_id')
        storage = create_autospec(ProjectStorageInterface)
        presenter = create_autospec(ProjectPresenterInterface)
        interactor = CreateProjectInteractor(storage=storage)

        storage.validate_workflow_id.return_value = False
        presenter.raise_invalid_workflow_id_exception.side_effect = \
            NotFound(*INVALID_WORKFLOW)

        #act

        with pytest.raises(NotFound) as error:
            interactor.create_project_wrapper(
                user_id=user_id,
                project_data=project_data,
                presenter=presenter
                )

        #assert
        error_message = str(error.value)
        storage.validate_workflow_id.assert_called_once_with(
            workflow_id=workflow_id)
        presenter.raise_invalid_workflow_id_exception.assert_called_once()
        snapshot.assert_match(error_message, 'error_message')
