from abc import abstractmethod, ABC
from typing import List

class MealStorageInterface(ABC):

    @abstractmethod
    def validate_meal_id(self, meal_id):
        pass

    @abstractmethod
    def get_items_of_meal(self, meal_id):
        pass

    @abstractmethod
    def validate_item_id(self, item_id):
        pass

    @abstractmethod
    def validate_meal_preference_date(
        self,
        set_preference_for_date):
        pass

    @abstractmethod
    def get_items_quantities(self, item_ids: List, meal_id: int):
        pass
