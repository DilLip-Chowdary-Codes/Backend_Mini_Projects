import pytest
from freezegun import freeze_time
from project_management_portal.storages.project_storage_implementation\
    import ProjectStorageImplementation
from project_management_portal.tests.storages.raw_inputs\
    import project_dto, projects_dtos,\
            projects_details_dtos,\
            project_details_dto

@freeze_time("2020-05-28 10:06:23")
@pytest.mark.django_db
class TestProjectStorage:

    def test_validate_workflow_id_with_valid_id(self, workflows):

        #arrange
        storage = ProjectStorageImplementation()
        workflow_id = 1
        expected_is_workflow_valid = True

        #act
        is_workflow_valid = storage.validate_workflow_id(
            workflow_id=workflow_id)

        #assert
        assert is_workflow_valid == expected_is_workflow_valid

    def test_validate_workflow_id_with_invalid_id(self, workflows):

        #arrange
        storage = ProjectStorageImplementation()
        workflow_id = 100
        expected_is_workflow_valid = False

        #act
        is_workflow_valid = storage.validate_workflow_id(
            workflow_id=workflow_id)

        #assert
        assert is_workflow_valid == expected_is_workflow_valid

    def test_validate_admin_scope_valid_id(self, users):

        #arrange
        user = users[0]
        user_id = user.user_id
        storage = ProjectStorageImplementation()
        expected_is_admin = True

        #act
        is_admin = storage.validate_admin_scope(user_id=user_id)

        #assert
        assert is_admin == expected_is_admin

    def test_validate_admin_scope_invalid_id(self, users):

        #arrange
        user = users[1]
        user_id = user.user_id
        storage = ProjectStorageImplementation()
        expected_is_admin = False

        #act
        is_admin = storage.validate_admin_scope(user_id=user_id)

        #assert
        assert is_admin == expected_is_admin

    def test_validate_project_id_with_valid_id(self, projects):

        #arrange
        from .expected_responses import project_dto
        storage = ProjectStorageImplementation()
        project_id = 1
        expected_is_project_valid = project_dto

        #act
        is_project_valid = storage.validate_project_id(
            project_id=project_id)

        #assert
        assert is_project_valid == expected_is_project_valid

    def test_validate_project_id_with_invalid_id(self, projects):

        #arrange
        storage = ProjectStorageImplementation()
        project_id = 100
        expected_is_project_valid = None

        #act
        is_project_valid = storage.validate_project_id(
            project_id=project_id)

        #assert
        assert is_project_valid == expected_is_project_valid

    def test_validate_developer_for_project_with_valid_id(self, projects):

        #arrange
        storage = ProjectStorageImplementation()
        developer_user_id = 2
        project_id = 1
        expected_is_developer_valid = True

        #act
        is_developer_valid = storage.validate_developer_for_project(
            user_id=developer_user_id,
            project_id=project_id)

        #assert
        assert is_developer_valid == expected_is_developer_valid

    def test_validate_developer_for_project_with_valid_admin_id(self, projects):

        #arrange
        storage = ProjectStorageImplementation()
        admin_user_id = 1
        project_id = 1
        expected_is_developer_valid = True

        #act
        is_developer_valid = storage.validate_developer_for_project(
            user_id=admin_user_id,
            project_id=project_id)

        #assert
        assert is_developer_valid == expected_is_developer_valid

    def test_validate_developer_for_project_with_invalid_id(self, projects):

        #arrange
        storage = ProjectStorageImplementation()
        developer_user_id = 3
        project_id = 1
        expected_is_developer_valid = False

        #act
        is_developer_valid = storage.validate_developer_for_project(
            user_id=developer_user_id,
            project_id=project_id)

        #assert
        assert is_developer_valid == expected_is_developer_valid

    def test_create_project(self, users, workflows):

        #arrange
        from project_management_portal.tests.storages.raw_inputs\
            import  project_details_dto
        user = users[0]
        user_id = user.user_id
        storage = ProjectStorageImplementation()
        expected_project_details_dto = project_details_dto

        #act
        project_details_dto = storage.create_project(
            user_id=user_id,
            project_dto=project_dto
            )

        #assert
        assert project_details_dto == expected_project_details_dto

    def test_create_project_with_no_developers(self, users, workflows):

        #arrange
        from .raw_inputs\
            import  project_details_with_no_developers_dto,\
                    project_with_no_developers_dto
        project_dto = project_with_no_developers_dto
        user = users[0]
        user_id = user.user_id
        storage = ProjectStorageImplementation()
        expected_project_details_dto = project_details_with_no_developers_dto

        #act
        project_details_dto = storage.create_project(
            user_id=user_id,
            project_dto=project_dto
            )

        #assert
        assert project_details_dto == expected_project_details_dto

    def test_get_user_projects_count(self, projects):

        #arrange
        user_id = 2
        storage = ProjectStorageImplementation()
        expected_response = 2

        #act
        response = storage.get_user_projects_count(user_id)

        #assert
        assert response == expected_response


    def test_get_user_projects_count_with_no_projects(self, users):

        #arrange
        user_id = 2
        storage = ProjectStorageImplementation()
        expected_response = 0

        #act
        response = storage.get_user_projects_count(user_id)

        #assert
        assert response == expected_response

    def test_get_admin_projects_count(self, projects):

        #arrange
        user_id = 1
        storage = ProjectStorageImplementation()
        expected_response = 2

        #act
        response = storage.get_admin_projects_count(user_id)

        #assert
        assert response == expected_response


    def test_get_admin_projects_count_with_no_projects(self, users):

        #arrange
        user_id = 1
        storage = ProjectStorageImplementation()
        expected_response = 0

        #act
        response = storage.get_admin_projects_count(user_id)

        #assert
        assert response == expected_response

    def test_validate_transition_with_valid_transition(self, projects):

        #arrange
        workflow_id = 1
        from_state_id = 1
        to_state_id = 2
        storage = ProjectStorageImplementation()
        expected_response = True

        #act
        response = storage.validate_transition(
            workflow_id,
            from_state_id,
            to_state_id)

        #assert
        assert response == expected_response

    def test_validate_transition_with_invalid_transition(self, projects):

        #arrange
        workflow_id = 1
        from_state_id = 2
        to_state_id = 1
        storage = ProjectStorageImplementation()
        expected_response = False

        #act
        response = storage.validate_transition(
            workflow_id,
            from_state_id,
            to_state_id)

        #assert
        assert response == expected_response

    def test_get_projects_for_user(self, projects):

        #arrange
        from project_management_portal.tests.storages.expected_responses\
            import user_projects_details_dtos
        user_id = 2
        storage = ProjectStorageImplementation()
        expected_user_projects_details = user_projects_details_dtos

        #act
        user_projects_details_dtos = storage.get_projects_for_user(
            user_id=user_id,
            limit=2,
            offset=0)

        #assert
        assert user_projects_details_dtos == expected_user_projects_details

    def test_get_projects_for_user_with_limit_1(self, projects):

        #arrange
        from project_management_portal.tests.storages.expected_responses\
            import user_projects_details_dtos
        user_id = 2
        storage = ProjectStorageImplementation()
        expected_user_projects_details = [user_projects_details_dtos[0]]

        #act
        user_projects_details_dtos = storage.get_projects_for_user(
            user_id=user_id,
            limit=1,
            offset=0)

        #assert


        assert user_projects_details_dtos == expected_user_projects_details

    def test_get_projects_for_user_with_offset_1(self, projects):

        #arrange
        from project_management_portal.tests.storages.expected_responses\
            import user_projects_details_dtos
        user_id = 2
        storage = ProjectStorageImplementation()
        expected_user_projects_details = [user_projects_details_dtos[1]]

        #act
        user_projects_details_dtos = storage.get_projects_for_user(
            user_id=user_id,
            limit=2,
            offset=1)

        #assert


        assert user_projects_details_dtos == expected_user_projects_details

    def test_get_projects_for_user_with_offset_gt_total_ptojects(
        self, projects):

        #arrange
        user_id = 2
        storage = ProjectStorageImplementation()
        expected_user_projects_details = []

        #act
        user_projects_details_dtos = storage.get_projects_for_user(
            user_id=user_id,
            limit=2,
            offset=3)

        #assert


        assert user_projects_details_dtos == expected_user_projects_details

    def test_get_projects_for_admin(self, projects):

        #arrange
        user_id = 1
        storage = ProjectStorageImplementation()
        from project_management_portal.tests.storages.expected_responses\
            import user_projects_details_dtos
        expected_user_projects_details = user_projects_details_dtos

        #act
        user_projects_details_dtos = storage.get_projects_for_admin(
            user_id=user_id,
            limit=2,
            offset=0)

        #assert

        print(user_projects_details_dtos)
        print("\n", expected_user_projects_details)

        assert user_projects_details_dtos == expected_user_projects_details

    def test_get_projects_for_admin_with_limit_1(self, projects):

        #arrange
        user_id = 1
        storage = ProjectStorageImplementation()
        from project_management_portal.tests.storages.expected_responses\
            import user_projects_details_dtos
        expected_user_projects_details = [user_projects_details_dtos[0]]

        #act
        user_projects_details_dtos = storage.get_projects_for_admin(
            user_id=user_id,
            limit=1,
            offset=0)

        #assert

        print(user_projects_details_dtos)
        print("\n", expected_user_projects_details)

        assert user_projects_details_dtos == expected_user_projects_details

    def test_get_projects_for_admin_with_offset_1(self, projects):

        #arrange
        user_id = 1
        storage = ProjectStorageImplementation()
        from project_management_portal.tests.storages.expected_responses\
            import user_projects_details_dtos
        expected_user_projects_details = [user_projects_details_dtos[1]]

        #act
        user_projects_details_dtos = storage.get_projects_for_admin(
            user_id=user_id,
            limit=2,
            offset=1)

        #assert

        print(user_projects_details_dtos)
        print("\n", expected_user_projects_details)

        assert user_projects_details_dtos == expected_user_projects_details

    def test_get_projects_for_admin_with_offset_gt_total_projects(
        self, projects):

        #arrange
        user_id = 1
        storage = ProjectStorageImplementation()
        expected_user_projects_details = []

        #act
        user_projects_details_dtos = storage.get_projects_for_admin(
            user_id=user_id,
            limit=2,
            offset=3)

        #assert

        print(user_projects_details_dtos)
        print("\n", expected_user_projects_details)

        assert user_projects_details_dtos == expected_user_projects_details

    def test_get_workflow_id_of_project(self, projects):

        #arrange
        storage = ProjectStorageImplementation()
        project_id = 1
        project = projects[0]
        expected_workflow_id = project.workflow_id

        #act
        workflow_id = storage.get_workflow_id_of_project(
            project_id=project_id)

        #assert
        assert workflow_id == expected_workflow_id

    def test_get_states_transition_details(self, projects):

        #arrange
        from .raw_inputs import get_transition_details_query_dto
        from .expected_responses import transition_details_dto
        storage = ProjectStorageImplementation()

        #act
        response = storage.get_states_transition_details(
            get_transition_details_query_dto)

        #assert
        assert response == transition_details_dto

    def test_get_states_transition_details_with_zero_checklist(
            self, projects):

        #arrange
        from .raw_inputs\
            import query_dto_with_no_checklist_for_transition
        from .expected_responses\
            import transition_details_with_no_checklist_dto
        storage = ProjectStorageImplementation()

        #act
        response = storage.get_states_transition_details(
            query_dto_with_no_checklist_for_transition)

        #assert
        assert response == transition_details_with_no_checklist_dto

    def test_get_transition_mandatory_checklist(self, projects):

        #arrange
        from .raw_inputs import update_task_state_query_dto
        from .expected_responses import transition_checklist_dtos
        storage = ProjectStorageImplementation()

        #act
        response = storage.get_transition_mandatory_checklist(
            update_task_state_query_dto)

        #assert
        print(response)
        print(transition_checklist_dtos)
        assert response == transition_checklist_dtos

    def test_get_transition_mandatory_checklist_with_empty(self, projects):

        #arrange
        from .raw_inputs\
            import update_task_state_query_expected_empty_checklist_dto
        from .expected_responses import transition_checklist_empty_dtos
        storage = ProjectStorageImplementation()

        #act
        response = storage.get_transition_mandatory_checklist(
            update_task_state_query_expected_empty_checklist_dto)

        #assert
        assert response == transition_checklist_empty_dtos
