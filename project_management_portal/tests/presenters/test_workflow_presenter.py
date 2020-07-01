from project_management_portal.presenters\
    .workflow_presenter_implementation\
        import WorkflowPresenterImplementation

class TestWorkFlowPresenter:
    def test_get_workflows_response(self, snapshot):

        #arrange
        from .raw_inputs import workflow_details_dtos
        presenter = WorkflowPresenterImplementation()

        #act
        workflow_details = presenter.get_workflows_response(workflow_details_dtos)

        #assert
        snapshot.assert_match(workflow_details, 'workflow_details')

    def test_get_workflows_response_with_no_workflows(self, snapshot):

        #arrange
        from .raw_inputs import workflow_details_dtos_empty
        presenter = WorkflowPresenterImplementation()

        #act
        workflow_details = presenter.get_workflows_response(
            workflow_details_dtos_empty)

        #assert
        snapshot.assert_match(workflow_details, 'workflow_details')
