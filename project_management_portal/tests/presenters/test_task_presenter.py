import pytest
from project_management_portal.presenters.task_presenter_implementation\
    import TaskPresenterImplementation
    
from django_swagger_utils.drf_server.exceptions\
    import NotFound, Unauthorized
from .raw_inputs import task_details_dto, tasks_details_dtos

from .expected_responses import task_details_response, tasks_details_response

class TestTaskPresenterImplementation:

    def test_raise_invalid_state_id_exception(self):

        #arrange
        presenter = TaskPresenterImplementation()
        
        #act
        with pytest.raises(NotFound) as e:
            presenter.raise_invalid_state_id_exception()

        #assert
        expected_err_message = "Invalid state_id, try with valid state_id"
        
        assert str(e.value) == expected_err_message

    def test_raise_invalid_task_id_exception(self):

        #arrange
        presenter = TaskPresenterImplementation()
        
        #act
        with pytest.raises(NotFound) as e:
            presenter.raise_invalid_task_id_exception()

        #assert
        expected_err_message = "Invalid Task, try with valid task"
        
        assert str(e.value) == expected_err_message

    def test_get_create_task_response(self):

        #arrange
        from .raw_inputs import task_details_dto
        presenter = TaskPresenterImplementation()
        task_details_dto = task_details_dto

        #act
        response = presenter.get_create_task_response(task_details_dto)

        #assert
        
        print(response)
        print("\n", task_details_response)
        assert response == task_details_response

    def test_get_tasks_response(self):

        #arrange
        from .raw_inputs import tasks_details_dtos
        from .expected_responses import tasks_details_response
        presenter = TaskPresenterImplementation()

        #act
        response = presenter.get_tasks_response(tasks_details_dtos)

        #assert
        print(response['tasks'])
        print("\n\n",tasks_details_response)
        assert response == tasks_details_response
    
    def test_get_task_states_response(self):

        #arrange
        from .raw_inputs import states_details_dtos
        from .expected_responses import task_states_response
        presenter = TaskPresenterImplementation()

        #act
        response = presenter\
            .get_task_states_response(
                states_details_dtos)

        #assert
        print(response)
        print("\n\n",task_states_response)
        assert response == task_states_response

    def test_get_task_states_response_with_no_states(self):

        #arrange
        from .raw_inputs import states_details_dtos_empty
        from .expected_responses import task_states_response_empty
        presenter = TaskPresenterImplementation()

        #act
        response = presenter\
            .get_task_states_response(
                states_details_dtos_empty)

        #assert
        print(response)
        print("\n\n",task_states_response_empty)
        assert response == task_states_response_empty
