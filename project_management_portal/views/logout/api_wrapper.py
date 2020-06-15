import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from project_management_portal.interactors.user_logout_interactor\
    import UserLogoutInteractor
from project_management_portal.presenters.user_presenter_implementation\
    import UserPresenterImplementation
from project_management_portal.storages.user_storage_implementation\
    import UserStorageImplementation

from .validator_class import ValidatorClass

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    storage = UserStorageImplementation()
    presenter = UserPresenterImplementation()
    interactor = UserLogoutInteractor(
        storage=storage,
        presenter=presenter
        )

    access_token = kwargs['access_token']
    login_response = interactor.logout(
        access_token=access_token
        )

    response_data = json.dumps(login_response)
    return HttpResponse(response_data, status=200)
