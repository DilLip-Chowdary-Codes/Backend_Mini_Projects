import pytest
from unittest.mock import create_autospec, Mock, patch

from project_management_portal.interactors.storages.project_storage_interface\
    import ProjectStorageInterface
from project_management_portal.interactors.presenters\
    .project_presenter_interface import ProjectPresenterInterface
from project_management_portal.interactors.get_projects_interactor\
    import GetProjectsInteractor
from .raw_inputs import project_data
from .expected_responses\
    import \
        get_projects_response,\
        projects_dtos

from project_management_portal.exceptions import InvalidWorkFlow
from project_management_portal.adapters.user_service import UserService

@pytest.mark.django_db
class TestGetProjects:

    @patch.object(UserService, 'interface')
    def test_get_projects_for_admin(self, interface_mock, snapshot):

        #arrange
        user_id = 1
        total_projects_count = 2
        project_storage = create_autospec(ProjectStorageInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)
        interactor = GetProjectsInteractor(project_storage=project_storage)
        project_storage.get_projects_for_admin.return_value\
            = projects_dtos
        project_storage.get_admin_projects_count.return_value\
            = total_projects_count
        project_presenter.get_projects_response\
            .return_value = get_projects_response
        interface_mock.is_user_admin.return_value=True

        #act
        project_details = interactor.get_projects_wrapper(
            user_id=user_id,
            offset=0,
            limit=1,
            project_presenter=project_presenter
            )

        #assert
        project_storage.get_projects_for_admin.assert_called_once_with(
                user_id=user_id,
                offset=0,
                limit=1)
        project_presenter.get_projects_response.assert_called_once_with(
            total_projects_count=total_projects_count,
            all_projects_details_dtos=projects_dtos)
        snapshot.assert_match(project_details, 'project_details')

    @patch.object(UserService, 'interface')
    def test_get_projects_for_normal_user(self, interface_mock, snapshot):

        user_id = 1
        total_projects_count = 2
        project_storage = create_autospec(ProjectStorageInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)
        interactor = GetProjectsInteractor(project_storage=project_storage)

        project_storage.get_projects_for_user.return_value\
            = projects_dtos
        project_storage.get_user_projects_count.return_value\
            = total_projects_count
        project_presenter.get_projects_response\
            .return_value = get_projects_response

        interface_mock.is_user_admin.return_value = False
        #act

        project_details = interactor.get_projects_wrapper(
            user_id=user_id,
                offset=0,
                limit=1,
                project_presenter=project_presenter)

        #assert
        project_storage.get_projects_for_user.assert_called_once_with(
                user_id=user_id,
                offset=0,
                limit=1)

        project_presenter.get_projects_response.assert_called_once_with(
            total_projects_count=total_projects_count,
            all_projects_details_dtos=projects_dtos)
        snapshot.assert_match(project_details, 'project_details')
