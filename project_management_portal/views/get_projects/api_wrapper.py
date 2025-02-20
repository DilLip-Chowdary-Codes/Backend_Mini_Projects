import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from project_management_portal.interactors.get_projects_interactor\
    import GetProjectsInteractor
from project_management_portal.presenters.project_presenter_implementation\
    import ProjectPresenterImplementation
from project_management_portal.storages.project_storage_implementation\
    import ProjectStorageImplementation
from project_management_portal.constants import DEFAULT_LIMIT, DEFAULT_OFFSET

from .validator_class import ValidatorClass

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    user = kwargs['user']
    query_params = kwargs['request_query_params'].__dict__

    project_storage = ProjectStorageImplementation()
    project_presenter = ProjectPresenterImplementation()
    interactor = GetProjectsInteractor(
        project_storage=project_storage
        )

    user_id = user.user_id
    limit = query_params.get('limit', DEFAULT_LIMIT)
    offset = query_params.get('offset', DEFAULT_OFFSET)

    projects_details = interactor.get_projects_wrapper(
        user_id=user_id,
        offset=offset,
        limit=limit,
        project_presenter=project_presenter
        )

    response_data = json.dumps(projects_details)
    return HttpResponse(response_data, status=200)
