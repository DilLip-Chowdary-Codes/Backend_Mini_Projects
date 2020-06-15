import pytest

from project_management_portal\
    .storages.workflow_storage_implementation\
    import WorkflowStorageImplementation

@pytest.mark.django_db
class TestWorkFlowStorage:

    def test_get_workflows(self, workflows):

        #arrange
        from .expected_responses import workflow_details_dtos
        storage = WorkflowStorageImplementation()

        #act
        response = storage.get_workflows()

        #assert
        assert response == workflow_details_dtos

    def test_get_workflows_with_no_workflows(self):

        #arrange

        storage = WorkflowStorageImplementation()
        expected_workflow_details_dtos = []

        #act
        response = storage.get_workflows()

        #assert
        assert response == expected_workflow_details_dtos

    def test_get_workflows_with_no_states(self, workflows_with_no_states):

        #arrange
        from .expected_responses import workflow_details_dtos_with_no_states
        storage = WorkflowStorageImplementation()

        #act
        response = storage.get_workflows()

        #assert
        print(response)
        print(workflow_details_dtos_with_no_states)
        assert response == workflow_details_dtos_with_no_states

    def test_get_workflows_with_no_transitions(
        self,
        workflows_with_no_transitions
        ):

        #arrange
        from .expected_responses\
            import workflow_details_dtos_with_no_transitions

        storage = WorkflowStorageImplementation()

        #act
        response = storage.get_workflows()

        #assert
        print(response)
        print(workflow_details_dtos_with_no_transitions)
        assert\
            response == workflow_details_dtos_with_no_transitions
