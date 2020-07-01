import pytest
from freezegun import freeze_time
from datetime import datetime

from user_app.models\
    import User
from oauth2_provider.models import AccessToken

@pytest.fixture()
def users():
    password = "admin@123"
    users_list = [
        User(
            username="username_1",
            is_admin=True,
            profile_pic="http://www.google.com",
            phone_no="9782346742"
            ),
        User(
            username="username_2",
            is_admin=False,
            profile_pic="http://www.google.com",
            phone_no="9782346742"
            ),
        User(
            username="username_3",
            is_admin=True,
            profile_pic="http://www.google.com",
            phone_no="9782346742"
            ),
            ]
    User.objects.bulk_create(users_list)
    users_objects = list(User.objects.all())
    for user in users_objects:
        user.set_password(password)
        user.save()

    return users_objects

@pytest.fixture
def access_tokens(users):
    access_tokens_list = [
        AccessToken(
            user_id=1,
            token="test_access_token",
            expires=datetime.now()
            )
        ]
    with freeze_time("2020-05-28 10:06:23"):
        AccessToken.objects.bulk_create(access_tokens_list)
    access_tokens_objs = AccessToken.objects.all()
    return access_tokens_objs
