from project_management_portal.interactors.storages.user_storage_interface \
    import UserStorageInterface
from project_management_portal.interactors\
    .presenters.user_presenter_interface \
    import UserPresenterInterface

class UserLogoutInteractor:

    def __init__(self,
                 storage: UserStorageInterface,
                 presenter: UserPresenterInterface
                ):
        self.storage = storage
        self.presenter = presenter

    def logout(self, access_token: str):
        is_token_valid = self.storage.validate_access_token(access_token)
        token_invalid = not is_token_valid

        if token_invalid:
            self.presenter.raise_invalid_access_token_exception()
        else:
            self.storage.delete_access_token(access_token)

        return self.presenter.logout_response()
