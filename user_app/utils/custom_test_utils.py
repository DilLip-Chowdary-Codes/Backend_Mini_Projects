from freezegun import freeze_time
from django_swagger_utils.utils.test import CustomAPITestCase
from user_app.utils.factories import UserFactory

class CustomTestUtils(CustomAPITestCase):

    def reset(self):
        UserFactory.reset_sequence(1)

    def create_user(self):
        self.reset()
        user = UserFactory()
        user.set_password('password')
        user.save()

    def create_user_admin(self):
        UserFactory.reset_sequence(1)
        admin = UserFactory(username='admin_1', is_admin=True)
        admin.set_password('password')
        admin.save()
        return admin

    def remove_token(self):
        from oauth2_provider.models import AccessToken
        # AccessToken.objects.filter(user_id=1).delete()
        print(AccessToken.objects.all())

    def user_auth_token_dto(self):
        from common.dtos import UserAuthTokensDTO
        auth_token_dto = UserAuthTokensDTO(
            user_id=1,
            access_token="test_access_token",
            refresh_token="test_refresh_token",
            expires_in=1000000
            )
        return auth_token_dto
