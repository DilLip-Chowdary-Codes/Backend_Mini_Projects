import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from user_app.interactors.user_logout_interactor\
    import UserLogoutInteractor
from user_app.presenters.user_presenter_implementation\
    import UserPresenterImplementation
from user_app.storages.user_storage_implementation\
    import UserStorageImplementation

from .validator_class import ValidatorClass

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    storage = UserStorageImplementation()
    presenter = UserPresenterImplementation()
    interactor = UserLogoutInteractor(storage=storage)

    access_token = kwargs['access_token']
    login_response = interactor.logout_wrapper(access_token=access_token,
                                               presenter=presenter
                                              )

    response_data = json.dumps(login_response)
    return HttpResponse(response_data, status=200)
