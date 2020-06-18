class InvalidDomainId(Exception):
    pass

class UserNotFollowingDomain(Exception):
    pass

class InvalidPostIdsException(Exception):
    def __init__(self, invalid_post_ids):
        self.invalid_post_ids = invalid_post_ids
