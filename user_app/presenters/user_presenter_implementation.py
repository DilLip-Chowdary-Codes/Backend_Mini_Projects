from user_app.interactors.presenters\
    .user_presenter_interface\
    import UserPresenterInterface
from user_app.constants.exception_messages\
    import INVALID_USER_ID, INVALID_USERNAME,\
           INVALID_PASSWORD, INVALID_ACCESS_TOKEN

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
            "expires_in": str(oauth_token_dto.expires_in)
        }

        return login_response

    def logout_response(self):
        response = {
            "status": "Logged out Succesfully"
        }
        return response

    def is_admin_response(self, is_admin: bool):
        response = {"is_admin": is_admin}
        return response

    def raise_invalid_user_id_exception(self):
        raise NotFound(*INVALID_USER_ID)
    
    def raise_invalid_user_ids_exception(self, invalid_user_ids):
        raise NotFound(
            "Invalid User Ids Given ",
            f"the following ids are Invalid{invalid_user_ids}"
            )
    
    def get_user_dto_response(self, userdto):
        user_details = {
            "user_id":userdto.user_id,
            "username":userdto.username,
            "profile_pic":userdto.profile_pic,
            "phone_no":userdto.phone_no
        }

        return user_details

    def get_user_dtos_response(self, user_dtos):
        users_details = [
            self.get_user_dto_response(userdto)
            for user_dto in user_dtos
            ]
        return users_details
