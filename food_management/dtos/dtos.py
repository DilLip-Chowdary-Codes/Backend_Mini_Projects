from typing import List
from dataclasses import dataclass
from food_management.constants.enums import MealType

@dataclass
class ItemDto:
    item_id: int
    quantity: int

@dataclass
class MealRequestDto:
    meal_id: int
    items: List[ItemDto]
    date: str
