import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from project_management_portal.interactors.task_state_transition_interactor\
    import TaskStateTransitionInteractor

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
    request_data = kwargs['request_data']

    project_storage = ProjectStorageImplementation()
    task_storage = TaskStorageImplementation()

    task_presenter = TaskPresenterImplementation()
    project_presenter = ProjectPresenterImplementation()

    interactor = TaskStateTransitionInteractor(
        project_storage=project_storage,
        task_storage=task_storage
        )

    project_id = kwargs['project_id']
    task_id = kwargs['task_id']
    checklist = request_data['checklist']

    user_id = user.user_id

    update_task_state_data = {
        "user_id": user_id,
        "project_id": project_id,
        "task_id": task_id,
        "from_state_id": request_data.get('from_state_id'),
        "to_state_id": request_data.get('to_state_id'),
        "checklist": checklist
    }

    task_details = interactor.update_task_state_wrapper(
        update_task_state_data,
        project_presenter=project_presenter,
        task_presenter=task_presenter)

    response_data = json.dumps(task_details)
    return HttpResponse(response_data, status=201)
