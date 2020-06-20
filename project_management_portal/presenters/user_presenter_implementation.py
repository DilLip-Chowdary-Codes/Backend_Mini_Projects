from project_management_portal.interactors.presenters\
    .user_presenter_interface\
    import UserPresenterInterface
from project_management_portal.constants.exception_messages\
    import INVALID_USERNAME, INVALID_PASSWORD, INVALID_ACCESS_TOKEN

from django_swagger_utils.drf_server.exceptions\
    import NotFound, Unauthorized

from common.dtos import UserAuthTokensDTO

class UserPresenterImplementation(UserPresenterInterface):

    def raise_invalid_username_exception(self):
        raise NotFound(*INVALID_USERNAME)

    def raise_invalid_password_exception(self):
        raise Unauthorized(*INVALID_PASSWORD)

    def raise_invalid_access_token_exception(self):
        raise Unauthorized(*INVALID_ACCESS_TOKEN)

    def get_login_response(self,
                           userdto,
                           oauth_token_dto: UserAuthTokensDTO
                          ):

        login_response = {
            "user_id": userdto.user_id,
            "username": userdto.username,
            "profile_pic": userdto.profile_pic,
            "is_admin": userdto.is_admin,
            "access_token": oauth_token_dto.access_token,
            "refresh_token": oauth_token_dto.refresh_token,
            "expires_in": oauth_token_dto.expires_in
        }

        return login_response

    def logout_response(self):
        response = {
            "status": "Logged out Succesfully"
        }
        return response
