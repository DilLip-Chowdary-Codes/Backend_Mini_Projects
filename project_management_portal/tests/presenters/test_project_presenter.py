import pytest
from project_management_portal.presenters.project_presenter_implementation\
    import ProjectPresenterImplementation
from project_management_portal.exceptions\
    import InvalidToken, InvalidWorkFlow
from django_swagger_utils.drf_server.exceptions\
    import NotFound, Unauthorized, BadRequest

from .raw_inputs import project_details_dto, projects_details_dtos

class TestProjectPresenter:

    def test_raise_invalid_workflow_id_exception(self, snapshot):

        #arrange
        presenter = ProjectPresenterImplementation()

        #act
        with pytest.raises(NotFound) as error:
            presenter.raise_invalid_workflow_id_exception()

        #assert
        error_message = str(error.value)
        snapshot.assert_match(error_message, 'error_message')

    def test_raise_invalid_project_id_exception(self, snapshot):

        #arrange
        presenter = ProjectPresenterImplementation()

        #act
        with pytest.raises(NotFound) as error:
            presenter.raise_invalid_project_id_exception()

        #assert
        error_message = str(error.value)
        snapshot.assert_match(error_message, 'error_message')

    def test_raise_invalid_transition_exception(self, snapshot):

        #arrange
        presenter = ProjectPresenterImplementation()

        #act
        with pytest.raises(NotFound) as error:
            presenter.raise_invalid_transition_exception()

        #assert
        error_message = str(error.value)
        snapshot.assert_match(error_message, 'error_message')

    def test_raise_unauthorized_developer_exception(self, snapshot):

        #arrange
        presenter = ProjectPresenterImplementation()

        #act
        with pytest.raises(Unauthorized) as error:
            presenter.raise_unauthorized_developer_exception()

        #assert
        error_message = str(error.value)
        snapshot.assert_match(error_message, 'error_message')

    def test_raise_invalid_limit_value_exception(self, snapshot):

        #arrange
        presenter = ProjectPresenterImplementation()

        #act
        with pytest.raises(BadRequest) as error:
            presenter.raise_invalid_limit_value_exception()

        #assert
        error_message = str(error.value)
        snapshot.assert_match(error_message, 'error_message')

    def test_raise_invalid_offset_value_exception(self, snapshot):

        #arrange
        presenter = ProjectPresenterImplementation()

        #act
        with pytest.raises(BadRequest) as error:
            presenter.raise_invalid_offset_value_exception()

        #assert
        error_message = str(error.value)
        snapshot.assert_match(error_message, 'error_message')

    def test_get_project_details_response(self, snapshot):

        #arrange
        presenter = ProjectPresenterImplementation()

        #act
        project_details = presenter.get_project_details_response(
            project_details_dto=project_details_dto)

        #assert
        snapshot.assert_match(project_details, 'project_details')

    def test_get_projects_response(self, snapshot):

        #arrange
        presenter = ProjectPresenterImplementation()

        #act
        projects_details = presenter.get_projects_response(
                total_projects_count=1,
                all_projects_details_dtos=projects_details_dtos)

        #assert
        snapshot.assert_match(projects_details, 'projects_details')

    def test_get_transition_details_response(self, snapshot):

        #arrange
        # from .raw_inputs import TransitionDetailsDto
        pass
        #act

        #assert
