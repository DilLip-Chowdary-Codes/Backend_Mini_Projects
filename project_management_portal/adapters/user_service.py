from typing import List
from project_management_portal.dtos import UserDto

class UserService:

    @property
    def interface(self):
        from user_app.interfaces.user_service_interface\
            import UserServiceInterface
        return UserServiceInterface()

    def is_admin(self, user_id: int):
        return self.interface.is_admin(user_id)

    def get_user_dto(self, user_id: int):
        user_dto = self.interface.get_user_dto(user_id)
        converted_user_dto = UserDto(
            user_id=user_dto.user_id,
            username=user_dto.username,
            profile_pic=user_dto.profile_pic,
            phone_no=user_dto.phone_no,
            is_admin=user_dto.is_admin
            )
        return converted_user_dto

    def get_user_dtos(self, user_ids: List[int]):

        user_dtos = self.interface.get_user_dtos(user_ids)
        converted_user_dtos = [
            UserDto(
            user_id=user_dto.user_id,
            username=user_dto.username,
            profile_pic=user_dto.profile_pic,
            phone_no=user_dto.phone_no,
            is_admin=user_dto.is_admin
            )
            for user_dto in user_dtos
            ]

        return converted_user_dtos
