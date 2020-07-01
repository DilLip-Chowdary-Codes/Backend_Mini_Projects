import pytest
from user_app.dtos import UserDto

@pytest.fixture
def user_dto():
    user_dto = UserDto(
        user_id=1,
        username="username_1",
        profile_pic="http://www.google.com",
        phone_no="8739835635",
        is_admin=True
        )
        
    return user_dto

@pytest.fixture
def user_admin_dto():
    user_admin_dto = UserDto(
        user_id=1,
        username="username_1",
        profile_pic="http://www.google.com",
        phone_no="8739835635",
        is_admin=True
        )
        
    return user_admin_dto
