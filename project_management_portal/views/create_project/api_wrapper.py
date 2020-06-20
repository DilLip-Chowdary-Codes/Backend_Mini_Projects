import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from project_management_portal.interactors.create_project_interactor\
    import CreateProjectInteractor
from project_management_portal.presenters.project_presenter_implementation\
    import ProjectPresenterImplementation
from project_management_portal.storages.project_storage_implementation\
    import ProjectStorageImplementation

from .validator_class import ValidatorClass

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    user = kwargs['user']
    request_data = kwargs['request_data']
    storage = ProjectStorageImplementation()
    presenter = ProjectPresenterImplementation()
    interactor = CreateProjectInteractor(
        storage=storage
        )

    user_id = user.user_id
    developers = request_data.get('developers')
    is_developers_empty = not developers
    if is_developers_empty:
        developers = []

    project_data = {
        "name": request_data['name'],
        "description": request_data['description'],
        "workflow_id": request_data['workflow_id'],
        "project_type": request_data['project_type'],
        "developers": developers
    }

    project_details = interactor.create_project_wrapper(
        user_id=user_id,
        project_data=project_data,
        presenter=presenter
        )
    project_details['success_message'] = "Project Created Succesfully"

    response_data = json.dumps(project_details)
    return HttpResponse(response_data, status=201)
