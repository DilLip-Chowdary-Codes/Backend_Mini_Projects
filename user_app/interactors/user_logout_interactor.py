from user_app.interactors.storages.user_storage_interface \
    import UserStorageInterface
from user_app.interactors\
    .presenters.user_presenter_interface \
    import UserPresenterInterface
from user_app.exceptions import InvalidToken

class UserLogoutInteractor:

    def __init__(self,
                 storage: UserStorageInterface
                ):
        self.storage = storage

    def logout_wrapper(self, access_token: str,
                       presenter: UserPresenterInterface
                      ):

        try:
            self.logout(access_token)

        except InvalidToken:
            presenter.raise_invalid_access_token_exception()

        return presenter.logout_response()

    def logout(self, access_token: str):
        is_token_valid = self.storage.validate_access_token(access_token)
        token_invalid = not is_token_valid

        if token_invalid:
            raise InvalidToken()
        else:
            self.storage.delete_access_token(access_token)
