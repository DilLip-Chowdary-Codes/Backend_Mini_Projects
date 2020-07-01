import pytest
from common.dtos import UserAuthTokensDTO
from datetime import datetime

@pytest.fixture
def OAuthTokenDto():
    oauth_dto = UserAuthTokensDTO(
        user_id=1,
    access_token="kjfewrfjbwg",
    refresh_token="sjdfbkgfsdg",
    expires_in=1000000
        )

    return oauth_dto
