from user_app.dtos import UserDto
import pytest

@pytest.fixture()
def user_dto():
    user_dto = UserDto(
        user_id=1,
        username="username_1",
        is_admin=False,
        profile_pic="http://www.google.com",
        phone_no="9999999999"
        )

    return user_dto

@pytest.fixture()
def user_admin_dto():
    user_admin_dto = UserDto(
        user_id=1,
        username="username_1",
        is_admin=True,
        profile_pic="http://www.google.com",
        phone_no="9999999999"
        )

    return user_admin_dto
