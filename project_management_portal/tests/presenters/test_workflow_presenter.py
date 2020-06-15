from project_management_portal.presenters\
    .workflow_presenter_implementation\
        import WorkflowPresenterImplementation

class TestWorkFlowPresenter:
    def test_get_workflows_response(self):

        #arrange
        from .raw_inputs import workflow_details_dtos
        from .expected_responses import workflow_details_dict
        presenter = WorkflowPresenterImplementation()

        #act
        response = presenter.get_workflows_response(workflow_details_dtos)

        #assert
        assert response == workflow_details_dict
    
    def test_get_workflows_response_with_no_workflows(self):

        #arrange
        from .raw_inputs import workflow_details_dtos_empty
        from .expected_responses import workflow_details_dict_empty
        presenter = WorkflowPresenterImplementation()

        #act
        response = presenter.get_workflows_response(
            workflow_details_dtos_empty)

        #assert
        assert response == workflow_details_dict_empty
