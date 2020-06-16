from enum import Enum
from ib_common.constants import BaseEnumClass

class MealType(BaseEnumClass, Enum):
    BREAKFAST = "BREAKFAST"
    LUNCH = "LUNCH"
    DINNER = "DINNER"
