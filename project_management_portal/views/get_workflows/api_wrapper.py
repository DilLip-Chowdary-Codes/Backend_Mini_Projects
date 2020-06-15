import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from project_management_portal.interactors.get_workflows_interactor\
    import GetWorkflowsInteractor
from project_management_portal.presenters.workflow_presenter_implementation\
    import WorkflowPresenterImplementation
from project_management_portal.storages.workflow_storage_implementation\
    import WorkflowStorageImplementation

from .validator_class import ValidatorClass

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    storage = WorkflowStorageImplementation()
    presenter = WorkflowPresenterImplementation()
    interactor = GetWorkflowsInteractor(
        workflow_storage=storage,
        workflow_presenter=presenter
        )

    workflows = interactor.get_workflows()
    
    response_data = json.dumps(workflows)
    return HttpResponse(response_data, status=200)
