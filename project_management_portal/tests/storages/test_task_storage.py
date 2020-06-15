import pytest
from project_management_portal.storages.task_storage_implementation\
    import TaskStorageImplementation

@pytest.mark.django_db
class TestTaskStorage:

    def test_validate_state_id(self, states):

        #arrange
        state_id = 1
        storage = TaskStorageImplementation()
        expected_is_state_valid = True

        #act
        is_state_valid = storage.validate_state_id(state_id=state_id)

        #assert
        assert is_state_valid == expected_is_state_valid

    def test_validate_state_id_with_invalid_value(self, states):

        #arrange
        state_id = 100
        storage = TaskStorageImplementation()
        expected_is_state_valid = False

        #act
        is_state_valid = storage.validate_state_id(state_id=state_id)

        #assert
        assert is_state_valid == expected_is_state_valid

    def test_validate_task_id(self, tasks):

        #arrange
        task_id = 1
        storage = TaskStorageImplementation()
        expected_is_task_valid = True

        #act
        is_task_valid = storage.validate_task_id(task_id=task_id)

        #assert
        assert bool(is_task_valid) == expected_is_task_valid


    def test_validate_task_id_with_invalid_id(self, tasks):

        #arrange
        task_id = 100
        storage = TaskStorageImplementation()
        expected_is_task_valid = None

        #act
        is_task_valid = storage.validate_task_id(task_id=task_id)

        #assert
        assert is_task_valid == expected_is_task_valid

    def test_create_task(self, users, projects, states):

        #arrange
        from .raw_inputs import task_dto
        from .expected_responses import task_details_dto
        user_id = 1
        storage = TaskStorageImplementation()

        #act
        response = storage.create_task(
            user_id=user_id,
            task_dto=task_dto)

        #assert
        print(response)
        print(task_details_dto)
        assert response == task_details_dto

    def test_get_tasks(self, tasks):

        #arrange
        from .expected_responses import tasks_details_dtos
        storage = TaskStorageImplementation()

        #act
        response = storage.get_tasks(
            project_id=1)

        #assert
        assert response == tasks_details_dtos

    def test_get_tasks_with_no_tasks(self):

        #arrange

        storage = TaskStorageImplementation()
        expected_tasks_details_dtos = []
        #act
        response = storage.get_tasks(
            project_id=1)

        #assert
        assert response == expected_tasks_details_dtos

    def test_update_task_state(self,states, tasks):

        #arrange
        from project_management_portal.models import Task
        storage = TaskStorageImplementation()
        task_id = 1
        updated_state_id = 2
        expected_state = states[1].name
        satisfied_checkpoints_ids = [1, 2]
        expected_conditions_satisfied = satisfied_checkpoints_ids

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
        assert updated_task_dto.state == expected_state
        assert conditions_satisfied == expected_conditions_satisfied

    def test_update_task_state_with_zero_satisfied_conditions(
            self,states, tasks):

        #arrange
        from project_management_portal.models import Task
        storage = TaskStorageImplementation()
        task_id = 1
        updated_state_id = 3
        expected_state = states[2].name
        satisfied_checkpoints_ids = []
        expected_conditions_satisfied = satisfied_checkpoints_ids

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
        assert updated_task_dto.state == expected_state
        assert conditions_satisfied == expected_conditions_satisfied

    def test_get_states_for_task_based_on_current_state(
            self,
            projects, tasks):

        #arrange
        from .expected_responses import available_states_dtos

        task_id = 1
        current_state_id = 1
        storage = TaskStorageImplementation()

        #act
        response = storage.get_states_for_task_based_on_current_state(
            task_id,
            current_state_id)

        #assert
        print(response)
        print(available_states_dtos)
        assert response == available_states_dtos

    def test_get_states_for_task_based_on_current_state_no_states(
        self,
        projects_with_no_transitions_for_state,
        tasks_with_projects_having_no_transition_state):

        #arrange
        from project_management_portal.models import Project
        projs = Project.objects.all()
        print("****Projects:-",projs)
        from .expected_responses import available_states_dtos_empty

        task_id = 1
        current_state_id = 1
        storage = TaskStorageImplementation()

        #act
        response = storage.get_states_for_task_based_on_current_state(
            task_id,
            current_state_id)

        #assert
        assert response == available_states_dtos_empty
