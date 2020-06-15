import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from project_management_portal.interactors.create_task_interactor\
    import CreateTaskInteractor

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
    interactor = CreateTaskInteractor(
        project_storage=project_storage,
        task_storage=task_storage,
        project_presenter=project_presenter,
        task_presenter=task_presenter
        )
    print("*"*100,"\n"*5,request_data['state_id'],"\n"*10)
    project_id = kwargs['project_id']
    user_id = user.user_id
    task_data = {
        "project_id": project_id,
        "issue_type": request_data['issue_type'],
        "title": request_data['title'],
        "description": request_data['description'],
        "state_id": request_data['state_id']
    }

    task_details = interactor.create_task(
        user_id=user_id,
        task_data=task_data
        )

    response_data = json.dumps(task_details)
    return HttpResponse(response_data, status=201)
