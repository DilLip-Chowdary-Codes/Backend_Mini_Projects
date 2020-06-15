from project_management_portal.interactors.storages\
    .workflow_storage_interface import WorkflowStorageInterface
from project_management_portal.interactors.presenters\
    .workflow_presenter_interface import WorkflowPresenterInterface

class GetWorkflowsInteractor:

    def __init__(
        self,
        workflow_storage: WorkflowStorageInterface,
        workflow_presenter: WorkflowPresenterInterface):

        self.workflow_storage = workflow_storage
        self.workflow_presenter = workflow_presenter

    def get_workflows(self):

        workflow_dtos = self.workflow_storage.get_workflows()
        workflows_dict = self.workflow_presenter.get_workflows_response(
            workflow_dtos)

        return workflows_dict
