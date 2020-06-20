from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from project_management_portal.interactors.storages.user_storage_interface \
    import UserStorageInterface
from project_management_portal.interactors.presenters.user_presenter_interface \
    import UserPresenterInterface
from project_management_portal.exceptions\
    import InvalidUsername, InvalidPassword

class UserLoginInteractor:

    def __init__(self,
                 storage: UserStorageInterface,
                 oauth_storage: OAuth2SQLStorage
                ):
        self.storage = storage
        self.oauth_storage = oauth_storage

    def login_wrapper(self, username: str, password: str,
                      presenter: UserPresenterInterface):
        try:
            userdto, oauth_token_dto = self.login(username, password)

        except InvalidUsername:
            presenter.raise_invalid_username_exception()
        except InvalidPassword:
            presenter.raise_invalid_password_exception()

        response = presenter.get_login_response(
            userdto,
            oauth_token_dto=oauth_token_dto
            )

        return response

    def login(self, username: str, password: str):
        user_id = self.storage.validate_username(username=username)
        username_invalid = not user_id

        if username_invalid:
            raise InvalidUsername()

        is_password_invalid = not self.storage.validate_login_credentials(
            username=username,
            password=password
            )

        if is_password_invalid:
            raise InvalidPassword()

        oauth_service = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth_storage
            )

        oauth_token_dto = oauth_service.create_user_auth_tokens(user_id=user_id)

        userdto = self.storage.get_user_details(user_id)
        return userdto, oauth_token_dto
