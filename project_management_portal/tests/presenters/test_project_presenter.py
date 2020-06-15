import pytest
from project_management_portal.presenters.project_presenter_implementation\
    import ProjectPresenterImplementation
from project_management_portal.exceptions\
    import InvalidToken, InvalidWorkFlow
from django_swagger_utils.drf_server.exceptions\
    import NotFound, Unauthorized, BadRequest

from .raw_inputs import project_details_dto, projects_details_dtos
from .expected_responses import get_project_response, get_projects_response

class TestProjectPresenter:

    def test_raise_invalid_workflow_id_exception(self):

        #arrange
        presenter = ProjectPresenterImplementation()
        expected_err_message = \
            "Invalid workflow, try with valid workflow"

        #act
        with pytest.raises(NotFound) as error:
            presenter.raise_invalid_workflow_id_exception()

        #assert
        assert str(error.value) == expected_err_message

    def test_raise_invalid_project_id_exception(self):

        #arrange
        presenter = ProjectPresenterImplementation()
        expected_err_message = \
            "Invalid project_id, try with valid project_id"

        #act
        with pytest.raises(NotFound) as error:
            presenter.raise_invalid_project_id_exception()

        #assert
        assert str(error.value) == expected_err_message

    def test_raise_invalid_transition_exception(self):

        #arrange
        presenter = ProjectPresenterImplementation()
        expected_err_message = \
            "Invalid Transition, try with valid transition"

        #act
        with pytest.raises(NotFound) as error:
            presenter.raise_invalid_transition_exception()

        #assert
        assert str(error.value) == expected_err_message

    def test_raise_unauthorized_developer_exception(self):

        #arrange
        presenter = ProjectPresenterImplementation()
        expected_err_message = \
            "Developer not allowed to access this resource"

        #act
        with pytest.raises(Unauthorized) as error:
            presenter.raise_unauthorized_developer_exception()

        #assert
        assert str(error.value) == expected_err_message

    def test_raise_invalid_limit_value_exception(self):

        #arrange
        presenter = ProjectPresenterImplementation()
        expected_err_message\
            = "Invalid limit value in query , try with valid values"

        #act
        with pytest.raises(BadRequest) as error:
            presenter.raise_invalid_limit_value_exception()

        #assert
        print(error.value.message)
        assert error.value.message == expected_err_message

    def test_raise_invalid_offset_value_exception(self):

        #arrange
        presenter = ProjectPresenterImplementation()
        expected_err_message\
            = "Invalid offset value in query , try with valid values"

        #act
        with pytest.raises(BadRequest) as error:
            presenter.raise_invalid_offset_value_exception()

        #assert
        print(error.value.message)
        assert error.value.message == expected_err_message

    def test_get_project_details_response(self):

        #arrange
        presenter = ProjectPresenterImplementation()

        #act
        response = presenter.get_project_details_response(
            project_details_dto=project_details_dto)

        #assert

        print(response)
        print("\n\n",get_project_response)
        assert response == get_project_response

    def test_get_projects_response(self):

        #arrange
        presenter = ProjectPresenterImplementation()

        #act
        response = presenter.get_projects_response(
                total_projects_count=1,
                all_projects_details_dtos=projects_details_dtos)

        #assert
        assert response == get_projects_response
    
    def test_get_transition_details_response(self):

        #arrange
        from .raw_inputs import TransitionDetailsDto
        #act

        #assert
