import pytest
from unittest.mock import create_autospec

from project_management_portal.interactors.get_workflows_interactor\
    import GetWorkflowsInteractor
from project_management_portal.interactors.storages\
    .workflow_storage_interface import WorkflowStorageInterface
from project_management_portal.interactors.presenters\
    .workflow_presenter_interface import WorkflowPresenterInterface


class TestGetWorkflowsInteractor:

    def test_get_workflows_interactor(self):

        #arrange
        from .expected_responses\
            import workflows_details_dtos, workflows_details

        workflow_storage = create_autospec(WorkflowStorageInterface)
        workflow_presenter = create_autospec(WorkflowPresenterInterface)
        interactor = GetWorkflowsInteractor(workflow_storage=workflow_storage)
        workflow_storage.get_workflows\
            .return_value = workflows_details_dtos
        workflow_presenter.get_workflows_response\
            .return_value = workflows_details

        #act
        response = interactor.get_workflows_wrapper(workflow_presenter)

        #assert
        workflow_storage.get_workflows.assert_called_once()
        workflow_presenter.get_workflows_response.assert_called_once_with(
            workflows_details_dtos)

        assert response == workflows_details
