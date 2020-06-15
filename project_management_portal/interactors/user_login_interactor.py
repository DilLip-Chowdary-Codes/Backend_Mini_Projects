from project_management_portal.interactors.storages.user_storage_interface \
    import UserStorageInterface
from project_management_portal.interactors.presenters.user_presenter_interface \
    import UserPresenterInterface
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService

class UserLoginInteractor:

    def __init__(self,
                 storage: UserStorageInterface,
                 oauth_storage: OAuth2SQLStorage,
                 presenter: UserPresenterInterface
                ):
        self.storage = storage
        self.presenter = presenter
        self.oauth_storage = oauth_storage

    def login(self, username: str, password: str):
        user_id = self.storage.validate_username(username=username)
        username_invalid = not user_id

        if username_invalid:
            self.presenter.raise_invalid_username_exception()

        is_password_invalid = not self.storage.validate_login_credentials(
            username=username,
            password=password
            )

        if is_password_invalid:
            self.presenter.raise_invalid_password_exception()

        oauth_service = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth_storage
            )

        oauth_token_dto = oauth_service.create_user_auth_tokens(user_id=user_id)

        userdto = self.storage.get_user_details(user_id)

        response = self.presenter.get_login_response(
            userdto,
            oauth_token_dto=oauth_token_dto
            )

        return response
