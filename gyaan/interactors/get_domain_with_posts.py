from gyaan.interactors.get_posts_details import GetPostsDetailsInteractor
from gyaan.interactors.get_domain_details import GetDomainDetailsInteractor

class GetDomainWithPostDetails:
    def __init__(self, get_posts_details, get_domain_details):
        self.get_posts_details = get_posts_details
        self.get_domain_details = get_domain_details
    
    def get_domain_with_posts(self, domain_id: int):
        