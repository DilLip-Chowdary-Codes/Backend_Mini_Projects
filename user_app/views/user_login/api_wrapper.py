import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from user_app.interactors.user_login_interactor\
    import UserLoginInteractor
from user_app.presenters.user_presenter_implementation\
    import UserPresenterImplementation
from user_app.storages.user_storage_implementation\
    import UserStorageImplementation
from common.oauth2_storage import OAuth2SQLStorage

from .validator_class import ValidatorClass

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    request_data = kwargs['request_data']
    storage = UserStorageImplementation()
    presenter = UserPresenterImplementation()
    oauth_storage = OAuth2SQLStorage()
    interactor = UserLoginInteractor(storage=storage,
                                     oauth_storage=oauth_storage
                                    )

    username = request_data['username']
    password = request_data['password']

    login_response = interactor.login_wrapper(username=username,
                                              password=password,
                                              presenter=presenter
                                             )
    response_data = json.dumps(login_response)
    return HttpResponse(response_data, status=200)
