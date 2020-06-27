from project_management_portal.exceptions\
    import InvalidLimitValue, InvalidOffsetValue

class ValidationsMixin:
    
    def validate_limit(self, limit: int):
        
        is_limit_value_invalid = limit <= 0 or limit >=25
        if is_limit_value_invalid:
            raise InvalidLimitValue()

    def validate_offset(self, offset: int):

        is_offset_value_invalid = offset < 0
        if is_offset_value_invalid:
            raise InvalidOffsetValue()
