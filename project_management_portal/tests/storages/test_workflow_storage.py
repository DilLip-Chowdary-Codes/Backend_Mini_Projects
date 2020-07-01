import pytest

from project_management_portal\
    .storages.workflow_storage_implementation\
    import WorkflowStorageImplementation

@pytest.mark.django_db
class TestWorkFlowStorage:

    def test_get_workflows(self, workflows, snapshot):

        #arrange
        storage = WorkflowStorageImplementation()

        #act
        workflow_details_dtos = storage.get_workflows()

        #assert
        snapshot.assert_match(workflow_details_dtos, 'workflow_details_dtos')

    def test_get_workflows_with_no_workflows(self, snapshot):

        #arrange

        storage = WorkflowStorageImplementation()

        #act
        workflow_details_dtos = storage.get_workflows()

        #assert
        snapshot.assert_match(workflow_details_dtos, 'workflow_details_dtos')

    def test_get_workflows_with_no_states(self, workflows_with_no_states,
                                          snapshot
                                         ):

        #arrange
        storage = WorkflowStorageImplementation()

        #act
        workflow_details_dtos = storage.get_workflows()

        #assert
        snapshot.assert_match(workflow_details_dtos, 'workflow_details_dtos')

    def test_get_workflows_with_no_transitions(
        self,
        workflows_with_no_transitions,
        snapshot
        ):

        #arrange

        storage = WorkflowStorageImplementation()

        #act
        workflow_details_dtos = storage.get_workflows()

        #assert
        snapshot.assert_match(workflow_details_dtos, 'workflow_details_dtos')
