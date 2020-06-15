import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from project_management_portal.interactors.user_login_interactor\
    import UserLoginInteractor
from project_management_portal.presenters.user_presenter_implementation\
    import UserPresenterImplementation
from project_management_portal.storages.user_storage_implementation\
    import UserStorageImplementation
from common.oauth2_storage import OAuth2SQLStorage

from .validator_class import ValidatorClass

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    request_data = kwargs['request_data']
    storage = UserStorageImplementation()
    presenter = UserPresenterImplementation()
    oauth_storage = OAuth2SQLStorage()
    interactor = UserLoginInteractor(
        storage=storage,
        oauth_storage=oauth_storage,
        presenter=presenter
        )
    username = request_data['username']
    password = request_data['password']

    login_response = interactor.login(
        username=username,
        password=password)
    print(login_response)
    response_data = json.dumps(login_response)
    return HttpResponse(response_data, status=200)
