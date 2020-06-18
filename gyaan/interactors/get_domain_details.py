from gyaan.interactors.storages.domain_storage_interface import StorageInterface
from gyaan.interactors.presenters.domain_presenter_interface\
    import PresenterInterface
from gyaan.exceptions import InvalidDomainId, UserNotFollowingDomain
from gyaan.interactors.dtos import DomainDetailsDTO

class GetDomainDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_details_wrapper(self, user_id: int, domain_id: int,
                                   presenter: PresenterInterface):
        try:
            domain_details_dto = self.get_domain_details(user_id, domain_id)

        except InvalidDomainId:
            presenter.raise_invalid_domain_id_exception()
        except UserNotFollowingDomain:
            presenter.raise_user_not_domain_member_exception()

        else:
            response = presenter.get_domain_details(domain_details_dto)
            return response

    def get_domain_details(self, user_id: int ,domain_id: int):

        domain_dto = self.storage.get_domain(domain_id)

        is_user_not_a_follower = not self.storage.is_user_following_domain(
            user_id, domain_id)
        if is_user_not_a_follower:
            raise UserNotFollowingDomain

        domain_expert_ids = self.storage.get_domain_expert_ids(domain_id)
        domain_experts = self.storage.get_users_details(domain_expert_ids)
        domain_stats = self.storage.get_domain_stats(domain_id)
        is_user_domain_expert = self.storage.is_user_domain_expert(user_id,
                                                                   domain_id
                                                                  )
        domain_details_dto = DomainDetailsDTO(
            domain=domain_dto,
            domain_stats=domain_stats,
            domain_experts=domain_experts,
            is_user_domain_expert=is_user_domain_expert
            )

        return domain_details_dto
