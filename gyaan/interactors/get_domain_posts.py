from gyaan.interactors.get_posts_details import GetPostsDetailsInteractor
from gyaan.interactors.storages.domain_storage_interface\
    import DomainStorageInterface
from gyaan.interactors.storages.post_storage_interface\
    import PostStorageInterface
from gyaan.interactors.presenters.domain_presenter_interface\
    import DomainPresenterInterface
from gyaan.interactors.presenters.post_presenter_interface\
    import PostPresenterInterface
from gyaan.exceptions \
    import UserNotFollowingDomain, InvalidPostIdsException, InvalidDomainId

class GetDomainPosts:
    def __init__(self,
                 domain_storage: DomainStorageInterface,
                 post_storage: PostStorageInterface):

        self.domain_storage = domain_storage
        self.post_storage = post_storage

    def get_domain_posts_wrapper(self, user_id: int, domain_id: int,
                                 limit: int, offset: int,
                                 domain_presenter: DomainPresenterInterface,
                                 post_presenter: PostPresenterInterface):
        try:
            domain_post_details_dto = self.get_domain_posts(user_id, domain_id,
                                                            limit, offset)
        except InvalidDomainId:
            domain_presenter.raise_invalid_domain_id_exception()
        except UserNotFollowingDomain:
            domain_presenter.raise_user_not_domain_member_exception()
        except InvalidPostIdsException as error:
            post_presenter.raise_invalid_post_ids_exception(
                error.invalid_post_ids)
        else:
            response = post_presenter.get_posts_details(domain_post_details_dto)
        return response

    def get_domain_posts(self, user_id: int, domain_id: int,
                         limit: int, offset: int):
        self.domain_storage.validate_domain_id(domain_id)

        is_user_not_a_follower = not self.domain_storage.is_user_following_domain(
            user_id, domain_id)
        if is_user_not_a_follower:
            raise UserNotFollowingDomain
        domain_post_ids = self.domain_storage.get_domain_post_ids(domain_id)

        get_posts_interactor = GetPostsDetailsInteractor(self.post_storage)
        domain_post_details_dto = get_posts_interactor.get_posts_details(
            domain_post_ids)

        return domain_post_details_dto
