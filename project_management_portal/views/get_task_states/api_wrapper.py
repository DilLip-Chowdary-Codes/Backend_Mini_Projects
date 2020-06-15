import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from project_management_portal.interactors.get_states_for_task_interactor\
    import GetStatesForTaskInteractor

from project_management_portal.presenters.project_presenter_implementation\
    import ProjectPresenterImplementation
from project_management_portal.presenters.task_presenter_implementation\
    import TaskPresenterImplementation

from project_management_portal.storages.project_storage_implementation\
    import ProjectStorageImplementation
from project_management_portal.storages.task_storage_implementation\
    import TaskStorageImplementation

from .validator_class import ValidatorClass

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    user = kwargs['user']
    project_id = kwargs['project_id']
    task_id = kwargs['task_id']

    project_storage = ProjectStorageImplementation()
    task_storage = TaskStorageImplementation()
    
    task_presenter = TaskPresenterImplementation()
    project_presenter = ProjectPresenterImplementation()
    interactor = GetStatesForTaskInteractor(
        project_storage=project_storage,
        task_storage=task_storage,
        project_presenter=project_presenter,
        task_presenter=task_presenter
        )

    task_state_data = {
        "user_id": user.user_id,
        "project_id": project_id,
        "task_id": task_id
    }

    task_states = interactor.get_states_for_task_based_on_current_state(
        task_state_data
        )

    response_data = json.dumps(task_states)
    return HttpResponse(response_data, status=200)
