from project_management_portal.interactors.storages\
    .workflow_storage_interface import WorkflowStorageInterface
from project_management_portal.interactors.presenters\
    .workflow_presenter_interface import WorkflowPresenterInterface

class GetWorkflowsInteractor:

    def __init__(
        self,
        workflow_storage: WorkflowStorageInterface):

        self.workflow_storage = workflow_storage

    def get_workflows_wrapper(self,
                              workflow_presenter: WorkflowPresenterInterface):

        try:
            workflow_dtos = self.get_workflows()

        except:
            pass

        workflows_dict = workflow_presenter.get_workflows_response(
            workflow_dtos)

        return workflows_dict

    def get_workflows(self):

        workflow_dtos = self.workflow_storage.get_workflows()
        return workflow_dtos
