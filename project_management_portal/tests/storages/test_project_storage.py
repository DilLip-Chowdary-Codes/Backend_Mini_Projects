import pytest
from unittest.mock import patch
from freezegun import freeze_time

from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.storages.project_storage_implementation\
    import ProjectStorageImplementation
from project_management_portal.tests.storages.raw_inputs\
    import project_dto, projects_dtos,\
            projects_details_dtos,\
            projects_details_dto
from project_management_portal.adapters.user_service\
            import UserService

@freeze_time("2020-05-28 10:06:23")
@pytest.mark.django_db
class TestProjectStorage:

    def test_validate_workflow_id_with_valid_id(self, workflows, snapshot):

        #arrange
        storage = ProjectStorageImplementation()
        workflow_id = 1

        #act
        is_workflow_valid = storage.validate_workflow_id(
            workflow_id=workflow_id)

        #assert
        snapshot.assert_match(is_workflow_valid, 'is_workflow_valid')

    def test_validate_workflow_id_with_invalid_id(self, workflows, snapshot):

        #arrange
        storage = ProjectStorageImplementation()
        workflow_id = 100

        #act
        is_workflow_valid = storage.validate_workflow_id(
            workflow_id=workflow_id)

        #assert
        snapshot.assert_match(is_workflow_valid, 'is_workflow_valid')

    def test_validate_project_id_with_valid_id(self, projects, snapshot):

        #arrange
        storage = ProjectStorageImplementation()
        project_id = 1

        #act
        project_dto = storage.validate_project_id(
            project_id=project_id)

        #assert
        snapshot.assert_match(project_dto, 'project_dto')

    def test_validate_project_id_with_invalid_id(self, projects, snapshot):

        #arrange
        storage = ProjectStorageImplementation()
        project_id = 100

        #act
        project_dto = storage.validate_project_id(
            project_id=project_id)

        #assert
        snapshot.assert_match(project_dto, 'project_dto')

    def test_validate_developer_for_project_with_valid_id(self, projects,
                                                          snapshot
                                                         ):

        #arrange
        storage = ProjectStorageImplementation()
        developer_user_id = 2
        project_id = 1

        #act
        is_developer_valid = storage.validate_developer_for_project(
            user_id=developer_user_id,
            project_id=project_id)

        #assert
        snapshot.assert_match(is_developer_valid, 'is_developer_valid')

    def test_validate_developer_for_project_with_valid_admin_id(self,
                                                                projects,
                                                                snapshot):

        #arrange
        storage = ProjectStorageImplementation()
        admin_user_id = 1
        project_id = 1

        #act
        is_developer_valid = storage.validate_developer_for_project(
            user_id=admin_user_id,
            project_id=project_id)

        #assert
        snapshot.assert_match(is_developer_valid, 'is_developer_valid')

    def test_validate_developer_for_project_with_invalid_id(self, projects,
                                                            snapshot):

        #arrange
        storage = ProjectStorageImplementation()
        developer_user_id = 3
        project_id = 1

        #act
        is_developer_valid = storage.validate_developer_for_project(
            user_id=developer_user_id,
            project_id=project_id)

        #assert
        snapshot.assert_match(is_developer_valid, 'is_developer_valid')

    @patch.object(UserService, 'interface')
    def test_create_project(self, interface_mock, workflows,
                            user_admin_dto, snapshot):

        #arrange
        from project_management_portal.tests.storages.raw_inputs\
            import  projects_details_dto
        user_id = 1
        storage = ProjectStorageImplementation()

        interface_mock.get_user_dto.return_value = user_admin_dto

        #act
        projects_details_dto = storage.create_project(
            user_id=user_id,
            project_dto=project_dto
            )

        #assert
        snapshot.assert_match(projects_details_dto, 'projects_details_dto')

    def test_create_project_with_no_developers(self, workflows,
                                               user_admin_dto,
                                               snapshot):

        #arrange
        from .raw_inputs\
            import  project_details_with_no_developers_dto,\
                    project_with_no_developers_dto
        project_dto = project_with_no_developers_dto
        user_id = 1
        storage = ProjectStorageImplementation()

        #act
        with patch.object(UserService, 'get_user_dto',
                          return_value=user_admin_dto):

            projects_details_dto = storage.create_project(
                user_id=user_id,
                project_dto=project_dto
                )

        #assert
        snapshot.assert_match(projects_details_dto, 'projects_details_dto')

    def test_get_user_projects_count(self, projects, snapshot):

        #arrange
        user_id = 2
        storage = ProjectStorageImplementation()

        #act
        response = storage.get_user_projects_count(user_id)

        #assert
        snapshot.assert_match(response, 'projects_count')

    def test_get_user_projects_count_with_no_projects(self, snapshot):

        #arrange
        user_id = 2
        storage = ProjectStorageImplementation()

        #act
        response = storage.get_user_projects_count(user_id)

        #assert
        snapshot.assert_match(response, 'projects_count')

    def test_get_admin_projects_count(self, projects, snapshot):

        #arrange
        user_id = 1
        storage = ProjectStorageImplementation()

        #act
        response = storage.get_admin_projects_count(user_id)

        #assert
        snapshot.assert_match(response, 'projects_count')

    def test_get_admin_projects_count_with_no_projects(self, snapshot):

        #arrange
        user_id = 1
        storage = ProjectStorageImplementation()

        #act
        response = storage.get_admin_projects_count(user_id)

        #assert
        snapshot.assert_match(response, 'projects_count')

    def test_validate_transition_with_valid_transition(self, projects,
                                                       snapshot
                                                      ):

        #arrange
        workflow_id = 1
        from_state_id = 1
        to_state_id = 2
        storage = ProjectStorageImplementation()

        #act
        response = storage.validate_transition(
            workflow_id,
            from_state_id,
            to_state_id)

        #assert
        snapshot.assert_match(response, 'is_transition_valid')

    def test_validate_transition_with_invalid_transition(self, projects,
                                                         snapshot
                                                        ):

        #arrange
        workflow_id = 1
        from_state_id = 2
        to_state_id = 1
        storage = ProjectStorageImplementation()

        #act
        response = storage.validate_transition(
            workflow_id,
            from_state_id,
            to_state_id)

        #assert
        snapshot.assert_match(response, 'is_transition_valid')

    @patch.object(UserService, 'interface')
    def test_get_projects_for_user(self, interface_mock, projects,
                                   user_admin_dto, snapshot):

        #arrange
        user_id = 2
        storage = ProjectStorageImplementation()
        interface_mock.get_user_dto.return_value=user_admin_dto

        #act
        user_projects_details_dtos = storage.get_projects_for_user(
            user_id=user_id,
            limit=2,
            offset=0)

        #assert
        snapshot.assert_match(user_projects_details_dtos,
                              'user_projects_details')

    @patch.object(UserService, 'interface')
    def test_get_projects_for_user_with_limit_1(self, interface_mock,
                                                projects, user_admin_dto,
                                                snapshot
                                               ):

        #arrange
        user_id = 2
        storage = ProjectStorageImplementation()
        interface_mock.get_user_dto.return_value = user_admin_dto

        #act
        user_projects_details_dtos = storage.get_projects_for_user(
            user_id=user_id,
            limit=1,
            offset=0)

        #assert
        snapshot.assert_match(user_projects_details_dtos,
                              'user_projects_details')

    @patch.object(UserService, 'interface')
    def test_get_projects_for_user_with_offset_1(self, interface_mock,
                                                 projects, user_admin_dto,
                                                 snapshot
                                                ):

        #arrange
        user_id = 2
        storage = ProjectStorageImplementation()
        interface_mock.get_user_dto.return_value = user_admin_dto

        #act
        user_projects_details_dtos = storage.get_projects_for_user(
            user_id=user_id,
            limit=2,
            offset=1)

        #assert


        snapshot.assert_match(user_projects_details_dtos,
                              'user_projects_details')

    @patch.object(UserService, 'interface')
    def test_get_projects_for_user_with_offset_gt_total_ptojects(
        self, interface_mock, projects, user_dto, snapshot):

        #arrange
        user_id = 2
        storage = ProjectStorageImplementation()
        interface_mock.get_user_dto.return_value=user_dto

        #act
        user_projects_details_dtos = storage.get_projects_for_user(
            user_id=user_id,
            limit=2,
            offset=3)

        #assert


        snapshot.assert_match(user_projects_details_dtos,
                              'user_projects_details')

    @patch.object(UserService, 'interface')
    def test_get_projects_for_admin(self, interface_mock, projects,
                                    user_admin_dto, snapshot):

        #arrange
        user_id = 1
        storage = ProjectStorageImplementation()
        interface_mock.get_user_dto.return_value=user_admin_dto

        #act
        admin_projects_details_dtos = storage.get_projects_for_admin(
            user_id=user_id,
            limit=2,
            offset=0)

        #assert

        snapshot.assert_match(admin_projects_details_dtos,
                              'user_projects_details')

    @patch.object(UserService, 'interface')
    def test_get_projects_for_admin_with_limit_1(self, interface_mock,
                                                 projects, user_admin_dto,
                                                 snapshot):

        #arrange
        user_id = 1
        storage = ProjectStorageImplementation()
        interface_mock.get_user_dto.return_value=user_admin_dto

        #act
        admin_projects_details_dtos = storage.get_projects_for_admin(
            user_id=user_id,
            limit=1,
            offset=0)

        #assert

        snapshot.assert_match(admin_projects_details_dtos,
                              'user_projects_details')

    @patch.object(UserService, 'interface')
    def test_get_projects_for_admin_with_offset_1(self, interface_mock,
                                                  projects, user_admin_dto,
                                                  snapshot):

        #arrange
        user_id = 1
        storage = ProjectStorageImplementation()
        interface_mock.get_user_dto.return_value=user_admin_dto

        #act
        admin_projects_details_dtos = storage.get_projects_for_admin(
            user_id=user_id,
            limit=2,
            offset=1)

        #assert

        snapshot.assert_match(admin_projects_details_dtos,
                              'user_projects_details')

    @patch.object(UserService, 'interface')
    def test_get_projects_for_admin_with_offset_gt_total_projects(
        self, interface_mock, projects, user_admin_dto, snapshot):

        #arrange
        user_id = 1
        storage = ProjectStorageImplementation()
        interface_mock.get_user_dto.return_value=user_admin_dto

        #act
        admin_projects_details_dtos = storage.get_projects_for_admin(
            user_id=user_id,
            limit=2,
            offset=3)

        #assert

        snapshot.assert_match(admin_projects_details_dtos,
                              'user_projects_details')

    def test_get_workflow_id_of_project(self, projects, snapshot):

        #arrange
        storage = ProjectStorageImplementation()
        project_id = 1

        #act
        workflow_id = storage.get_workflow_id_of_project(
            project_id=project_id)

        #assert
        snapshot.assert_match(workflow_id, 'workflow_id')

    def test_get_states_transition_details(self, projects, snapshot):

        #arrange
        from .raw_inputs import get_transition_details_query_dto
        storage = ProjectStorageImplementation()

        #act
        response = storage.get_states_transition_details(
            get_transition_details_query_dto)

        #assert
        snapshot.assert_match(response, 'transition_details_dto')

    def test_get_states_transition_details_with_zero_checklist(
            self, projects, snapshot):

        #arrange
        from .raw_inputs\
            import query_dto_with_no_checklist_for_transition
        storage = ProjectStorageImplementation()

        #act
        response = storage.get_states_transition_details(
            query_dto_with_no_checklist_for_transition)

        #assert
        snapshot.assert_match(response, 'transition_details')

    def test_get_transition_mandatory_checklist(self, projects, snapshot):

        #arrange
        from .raw_inputs import update_task_state_query_dto
        storage = ProjectStorageImplementation()

        #act
        response = storage.get_transition_mandatory_checklist(
            update_task_state_query_dto)

        #assert
        snapshot.assert_match(response, 'transition_checklist_dtos')

    def test_get_transition_mandatory_checklist_with_empty(self, projects,
                                                           snapshot):

        #arrange
        from .raw_inputs\
            import update_task_state_query_expected_empty_checklist_dto
        storage = ProjectStorageImplementation()

        #act
        response = storage.get_transition_mandatory_checklist(
            update_task_state_query_expected_empty_checklist_dto)

        #assert
        snapshot.assert_match(response, 'transition_checklist')
