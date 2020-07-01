from typing import  Union #Optional, List
from oauth2_provider.models import AccessToken
from user_app.interactors.storages.user_storage_interface \
    import UserStorageInterface
from user_app.models import User
from user_app.dtos import UserDto

class UserStorageImplementation(UserStorageInterface):

    def get_user_dto(self, user_id):

        user_obj = User.objects.get(user_id=user_id)
        userdto = self._convert_user_obj_to_dto(user_obj)
        return userdto
    
    def get_valid_user_ids(self, user_ids):
        valid_user_ids = User.objects\
            .filter(user_id__in=user_ids)\
            .values_list('user_id', flat=True)
        return valid_user_ids

    def get_user_dtos(self, user_ids):
        users = User.objects.filter(user_id__in=user_ids)
        user_dtos = [
            self._convert_user_obj_to_dto(user)
            for user in list(users)
            ]
        return user_dtos

    def validate_username(self, username: str) -> Union[bool, int]:

        user_not_exists = False

        try:
            user_id = User.objects.get(username=username).user_id
        except User.DoesNotExist:
            user_not_exists = True

        if user_not_exists:
            user_id = False

        return user_id

    def validate_login_credentials(self,
                                   username: str,
                                   password: str
                                  ) -> bool:
        user = User.objects.get(username=username)
        credentials_valid = user.check_password(password)

        return credentials_valid

    def validate_access_token(self, access_token: str) -> Union[bool, object]:

        try:
            token = AccessToken.objects.get(token=access_token)
        except AccessToken.DoesNotExist:
            token = None

        return token

    def delete_access_token(self, access_token: str):
        token = AccessToken.objects.get(token=access_token)
        token.delete()

    @staticmethod
    def _convert_user_obj_to_dto(user_obj):

        userdto = UserDto(
            user_id=user_obj.user_id,
            username=user_obj.username,
            profile_pic=user_obj.profile_pic,
            phone_no=user_obj.phone_no,
            is_admin=user_obj.is_admin
            )
        return userdto
