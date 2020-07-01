class InvalidUserId(Exception):
    pass

class InvalidUserIds(Exception):
    def __init__(self, invalid_user_ids):
        self.invalid_user_ids = invalid_user_ids

class InvalidUsername(Exception):
    pass

class InvalidPassword(Exception):
    pass

class InvalidToken(Exception):
    pass

class UnauthorizedUser(Exception):
    pass

class AccessForbidden(Exception):
    pass

class InvalidWorkFlow(Exception):
    pass

class InvalidProjectId(Exception):
    pass

class InvalidTaskId(Exception):
    pass

class InvalidLimitValue(Exception):
    pass

class InvalidOffsetValue(Exception):
    pass

class InvalidTransition(Exception):
    pass

class MandatoryChecklistNotChecked(Exception):
    pass
