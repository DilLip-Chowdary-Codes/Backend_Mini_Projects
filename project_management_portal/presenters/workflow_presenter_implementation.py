from project_management_portal.interactors\
    .presenters.workflow_presenter_interface\
        import WorkflowPresenterInterface

class WorkflowPresenterImplementation(WorkflowPresenterInterface):
    def get_workflows_response(self, workflow_details_dtos):

        workflows_dicts = [
            self._convert_workflow_details_dto_to_basic_details_dict(
                workflow_details_dto)
            for workflow_details_dto in workflow_details_dtos
            ]
        
        get_workflows_response = {
            "total_workflows": len(workflow_details_dtos),
            "workflows": workflows_dicts
        }
        
        
        return get_workflows_response
    
    @staticmethod
    def _convert_workflow_details_dto_to_basic_details_dict(
        workflow_details_dto):

        workflow_dict = {
            "workflow_id":workflow_details_dto.workflow_id,
            "name":workflow_details_dto.name
        }
        
        return workflow_dict
