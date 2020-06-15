import pytest
from unittest.mock import create_autospec, Mock

from project_management_portal.interactors.storages.project_storage_interface\
    import ProjectStorageInterface
from project_management_portal.interactors.presenters\
    .project_presenter_interface import ProjectPresenterInterface
from project_management_portal.interactors.get_projects_interactor\
    import GetProjectsInteractor
from .raw_inputs import project_data
from .expected_responses\
    import create_project_response,\
        get_projects_response,\
        project_dto,\
        projects_dtos

from project_management_portal.exceptions import InvalidWorkFlow

@pytest.mark.django_db
class TestGetProjects:

    def test_get_projects_for_admin(self):

        #arrange
        user_id = 1
        total_projects_count = 2
        project_storage = create_autospec(ProjectStorageInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)
        interactor = GetProjectsInteractor(
            project_storage=project_storage,
            project_presenter=project_presenter)

        project_storage.validate_admin_scope.return_value = True
        project_storage.get_projects_for_admin.return_value\
            = projects_dtos
        project_storage.get_admin_projects_count.return_value\
            = total_projects_count
        project_presenter.get_projects_response\
            .return_value = get_projects_response

        #act
        response = interactor.get_projects(
            user_id=user_id,
            offset=0,
            limit=1
            )

        #assert

        project_storage.validate_admin_scope.assert_called_once_with(
            user_id=user_id)
        project_storage.get_projects_for_admin.assert_called_once_with(
                user_id=user_id,
                offset=0,
                limit=1)

        project_presenter.get_projects_response.assert_called_once_with(
            total_projects_count=total_projects_count,
            all_projects_details_dtos=projects_dtos)
        assert response == get_projects_response

    def test_get_projects_for_normal_user(self):

        user_id = 1
        total_projects_count = 2
        project_storage = create_autospec(ProjectStorageInterface)
        project_presenter = create_autospec(ProjectPresenterInterface)
        interactor = GetProjectsInteractor(
            project_storage=project_storage,
            project_presenter=project_presenter)

        project_storage.validate_admin_scope.return_value = False
        project_storage.get_projects_for_user.return_value\
            = projects_dtos
        project_storage.get_user_projects_count.return_value\
            = total_projects_count
        project_presenter.get_projects_response\
            .return_value = get_projects_response

        #act

        response = interactor.get_projects(
            user_id=user_id,
                offset=0,
                limit=1)

        #assert
        project_storage.validate_admin_scope.assert_called_once_with(
            user_id=user_id)
        project_storage.get_projects_for_user.assert_called_once_with(
                user_id=user_id,
                offset=0,
                limit=1)

        project_presenter.get_projects_response.assert_called_once_with(
            total_projects_count=total_projects_count,
            all_projects_details_dtos=projects_dtos)
        assert response == get_projects_response
