import pytest
from project_management_portal.presenters.user_presenter_implementation\
    import UserPresenterImplementation
from django_swagger_utils.drf_server.exceptions\
    import NotFound, Unauthorized

class TestUserPresenter:

    def test_raise_invalid_username_exception(self):

        #arrange
        presenter = UserPresenterImplementation()
        #act
        with pytest.raises(NotFound):
            presenter.raise_invalid_username_exception()

        #assert

    def test_raise_invalid_password_exception(self):

        #arrange
        presenter = UserPresenterImplementation()
        #act
        with pytest.raises(Unauthorized):
            presenter.raise_invalid_password_exception()

        #assert

    def test_get_login_response(self, OAuthTokenDto):

        #arrange
        from .raw_inputs import user_dto
        from .expected_responses import login_response
        oauth_token_dto = OAuthTokenDto
        presenter = UserPresenterImplementation()

        #act
        response = presenter.get_login_response(
            user_dto,
            oauth_token_dto=oauth_token_dto)

        #assert
        print(response)
        print(login_response)
        assert response == login_response

    def test_raise_invalid_access_token_exception(self):

        #arrange
        presenter = UserPresenterImplementation()

        #act
        with pytest.raises(Unauthorized):
            presenter.raise_invalid_access_token_exception()

        #assert
