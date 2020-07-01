import pytest
from unittest.mock import patch
from project_management_portal.storages.task_storage_implementation\
    import TaskStorageImplementation
from project_management_portal.adapters.user_service import UserService

@pytest.mark.django_db
class TestTaskStorage:

    def test_validate_state_id(self, states, snapshot):

        #arrange
        state_id = 1
        storage = TaskStorageImplementation()

        #act
        is_state_valid = storage.validate_state_id(state_id=state_id)

        #assert
        snapshot.assert_match(is_state_valid, 'is_state_valid')

    def test_validate_state_id_with_invalid_value(self, states, snapshot):

        #arrange
        state_id = 100
        storage = TaskStorageImplementation()

        #act
        is_state_valid = storage.validate_state_id(state_id=state_id)

        #assert
        snapshot.assert_match(is_state_valid, 'is_state_valid')

    def test_validate_task_id(self, tasks, snapshot):

        #arrange
        task_id = 1
        storage = TaskStorageImplementation()

        #act
        task_dto = storage.validate_task_id(task_id=task_id)

        #assert
        snapshot.assert_match(task_dto, 'task_dto')

    def test_validate_task_id_with_invalid_id(self, tasks, snapshot):

        #arrange
        task_id = 100
        storage = TaskStorageImplementation()

        #act
        task_dto = storage.validate_task_id(task_id=task_id)

        #assert
        snapshot.assert_match(task_dto, 'task_dto')

    @patch.object(UserService, 'interface')
    def test_create_task(self, interface_mock,
                         projects, states, user_admin_dto,
                         snapshot):

        #arrange
        from .raw_inputs import task_dto
        from .expected_responses import task_details_dto
        user_id = 1
        storage = TaskStorageImplementation()
        interface_mock.get_user_dto.return_value = user_admin_dto

        #act
        task_details_dto = storage.create_task(
            user_id=user_id,
            task_dto=task_dto)

        #assert
        snapshot.assert_match(task_details_dto, 'task_details_dto')

    @patch.object(UserService, 'interface')
    def test_get_tasks(self, interface_mock, tasks, user_admin_dto, snapshot):

        #arrange
        storage = TaskStorageImplementation()
        interface_mock.get_user_dto.return_value = user_admin_dto

        #act
        tasks_details_dtos = storage.get_tasks(
            project_id=1)

        #assert
        snapshot.assert_match(tasks_details_dtos, 'tasks_details_dtos')

    @patch.object(UserService, 'interface')
    def test_get_tasks_with_no_tasks(self, interface_mock,
                                     user_admin_dto, snapshot):

        #arrange

        storage = TaskStorageImplementation()
        interface_mock.get_user_dto.return_value = user_admin_dto

        #act
        response = storage.get_tasks(
            project_id=1)

        #assert
        snapshot.assert_match(response, 'tasks_details_dtos')

    @patch.object(UserService, 'interface')
    def test_update_task_state(self, interface_mock, states,
                               tasks, user_admin_dto, snapshot):

        #arrange
        from project_management_portal.models import Task
        storage = TaskStorageImplementation()
        task_id = 1
        updated_state_id = 2
        satisfied_checkpoints_ids = [1, 2]
        interface_mock.get_user_dto.return_value = user_admin_dto

        #act
        updated_task_dto = storage.update_task_state(
            task_id=task_id,
            updated_state_id=updated_state_id,
            satisfied_checkpoints_ids=satisfied_checkpoints_ids)

        #assert

        task_obj = Task.objects.get(id=1)
        conditions_satisfied = list(task_obj
            .conditions_satisfied\
                .values_list('id', flat=True))

        snapshot.assert_match(conditions_satisfied, 'conditions_satisfied')
        snapshot.assert_match(updated_task_dto.state, 'state')

    @patch.object(UserService, 'interface')
    def test_update_task_state_with_zero_satisfied_conditions(
            self, interface_mock, states, tasks, user_admin_dto, snapshot):

        #arrange
        from project_management_portal.models import Task
        storage = TaskStorageImplementation()
        task_id = 1
        updated_state_id = 3
        satisfied_checkpoints_ids = []
        interface_mock.get_user_dto.return_value = user_admin_dto

        #act
        updated_task_dto = storage.update_task_state(
            task_id=task_id,
            updated_state_id=updated_state_id,
            satisfied_checkpoints_ids=satisfied_checkpoints_ids)

        #assert
        task_obj = Task.objects.get(id=1)
        conditions_satisfied = list(task_obj\
            .conditions_satisfied\
                .values_list('id', flat=True))
        snapshot.assert_match(updated_task_dto.state, 'state')
        snapshot.assert_match(conditions_satisfied,'conditions_satisfied')

    def test_get_states_for_task_based_on_current_state(
            self,
            projects, tasks, snapshot):

        #arrange

        task_id = 1
        current_state_id = 1
        storage = TaskStorageImplementation()

        #act
        states_dtos = storage.get_states_for_task_based_on_current_state(
            task_id,
            current_state_id)

        #assert
        snapshot.assert_match(states_dtos, 'states_dtos')

    def test_get_states_for_task_based_on_current_state_no_states(
        self,
        projects_with_no_transitions_for_state,
        tasks_with_projects_having_no_transition_state, snapshot):

        #arrange

        task_id = 1
        current_state_id = 1
        storage = TaskStorageImplementation()

        #act
        response = storage.get_states_for_task_based_on_current_state(
            task_id,
            current_state_id)

        #assert
        snapshot.assert_match(response, 'states_dtos')
