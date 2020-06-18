import pytest
from unittest.mock import Mock, create_autospec
from gyaan.interactors.storages.domain_storage_interface\
    import DomainStorageInterface
from gyaan.interactors.presenters.domain_presenter_interface\
    import DomainPresenterInterface
from gyaan.interactors.get_domain_details import GetDomainDetailsInteractor
from gyaan.exceptions import InvalidDomainId, UserNotFollowingDomain
from django_swagger_utils.drf_server.exceptions import BadRequest

class TestGetDomainDetails:

    def test_get_domain_details_with_invalid_domain_id_raises_exception(self):
        #arrange
        user_id = 1
        domain_id = 1
        storage = create_autospec(DomainStorageInterface)
        presenter = create_autospec(DomainPresenterInterface)
        interactor = GetDomainDetailsInteractor(storage)
        storage.get_domain.side_effect = InvalidDomainId
        presenter.raise_invalid_domain_id_exception.side_effect = BadRequest

        #act
        with pytest.raises(BadRequest):
            interactor.get_domain_details_wrapper(user_id, domain_id, presenter)
        #assert
        storage.get_domain.assert_called_once_with(domain_id)
        presenter.raise_invalid_domain_id_exception.assert_called_once()

    def test_get_domain_details_with_user_who_is_not_follower_raises_exception(
            self, domain_dto):
        #arrange
        user_id = 1
        domain_id = 1
        storage = create_autospec(DomainStorageInterface)
        presenter = create_autospec(DomainPresenterInterface)
        interactor = GetDomainDetailsInteractor(storage)
        storage.get_domain.return_value = domain_dto
        storage.is_user_following_domain.return_value = False
        presenter.raise_user_not_domain_member_exception\
            .side_effect = BadRequest

        #act
        with pytest.raises(BadRequest):
            interactor.get_domain_details_wrapper(user_id,
                                                  domain_id,
                                                  presenter)
        #assert
        storage.get_domain.assert_called_once_with(domain_id)
        storage.is_user_following_domain.assert_called_once_with(
            user_id, domain_id)
        presenter.raise_user_not_domain_member_exception.assert_called_once()

    def test_get_domain_details_with_valid_details(self, domain_dto,
                                                   domain_details_dto,
                                                   domain_details_response
                                                  ):
        #arrange
        user_id = 1
        domain_id = 1
        domain_expert_ids = [0 ,1, 2, 3, 4]
        domain_stats = domain_details_dto.domain_stats
        domain_experts = domain_details_dto.domain_experts
        is_user_domain_expert = False
        storage = create_autospec(DomainStorageInterface)
        presenter = create_autospec(DomainPresenterInterface)
        interactor = GetDomainDetailsInteractor(storage)
        storage.get_domain.return_value = domain_dto
        storage.is_user_following_domain.return_value = True
        storage.get_domain_expert_ids.return_value = domain_expert_ids
        storage.get_users_details.return_value = domain_experts
        storage.get_domain_stats.return_value = domain_stats
        storage.is_user_domain_expert.return_value = is_user_domain_expert
        presenter.get_domain_details.return_value = domain_details_response
        expected_response = domain_details_response

        #act
        response = interactor.get_domain_details_wrapper(user_id,
                                                  domain_id,
                                                  presenter)
        #assert
        storage.get_domain.assert_called_once_with(domain_id)
        storage.is_user_following_domain.assert_called_once_with(
            user_id, domain_id)
        storage.get_domain_expert_ids.assert_called_once_with(domain_id)
        storage.get_users_details.assert_called_once_with(domain_expert_ids)
        storage.get_domain_stats.assert_called_once_with(domain_id)
        storage.is_user_domain_expert.assert_called_once_with(user_id,
                                                              domain_id)
        presenter.get_domain_details.assert_called_once_with(
            domain_details_dto)
        assert response == expected_response
