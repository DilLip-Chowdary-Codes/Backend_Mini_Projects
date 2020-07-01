import pytest
from project_management_portal.presenters.task_presenter_implementation\
    import TaskPresenterImplementation

from django_swagger_utils.drf_server.exceptions\
    import NotFound, Unauthorized
from .raw_inputs import task_details_dto, tasks_details_dtos

class TestTaskPresenterImplementation:

    def test_raise_invalid_state_id_exception(self, snapshot):

        #arrange
        presenter = TaskPresenterImplementation()

        #act
        with pytest.raises(NotFound) as error:
            presenter.raise_invalid_state_id_exception()

        #assert
        error_message = str(error.value)
        snapshot.assert_match(error_message, 'error_message')

    def test_raise_invalid_task_id_exception(self, snapshot):

        #arrange
        presenter = TaskPresenterImplementation()

        #act
        with pytest.raises(NotFound) as error:
            presenter.raise_invalid_task_id_exception()

        #assert
        error_message = str(error.value)
        snapshot.assert_match(error_message, 'error_message')

    def test_get_create_task_response(self, snapshot):

        #arrange
        from .raw_inputs import task_details_dto
        presenter = TaskPresenterImplementation()
        task_details_dto = task_details_dto

        #act
        task_details = presenter.get_create_task_response(task_details_dto)

        #assert
        snapshot.assert_match(task_details, 'task_details')

    def test_get_tasks_response(self, snapshot):

        #arrange
        from .raw_inputs import tasks_details_dtos
        presenter = TaskPresenterImplementation()

        #act
        tasks_details = presenter.get_tasks_response(tasks_details_dtos)

        #assert
        snapshot.assert_match(tasks_details, 'tasks_details')

    def test_get_task_states_response(self, snapshot):

        #arrange
        from .raw_inputs import states_details_dtos
        presenter = TaskPresenterImplementation()

        #act
        task_states = presenter\
            .get_task_states_response(
                states_details_dtos)

        #assert
        snapshot.assert_match(task_states, 'task_states')

    def test_get_task_states_response_with_no_states(self, snapshot):

        #arrange
        from .raw_inputs import states_details_dtos_empty
        presenter = TaskPresenterImplementation()

        #act
        task_states = presenter\
            .get_task_states_response(
                states_details_dtos_empty)

        #assert
        snapshot.assert_match(task_states, 'task_states')
