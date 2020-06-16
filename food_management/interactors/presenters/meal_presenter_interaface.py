from abc import abstractmethod, ABC

class MealPresenterInterface(ABC):
    
    @abstractmethod
    def raise_invalid_meal_id_exception(self, error):
        pass

    @abstractmethod
    def raise_invalid_items_exception(self, error):
        pass
    
    @abstractmethod
    def raise_duplicate_items_exception(self, error):
        pass
    
    @abstractmethod
    def raise_invalid_quantity_for_items_exception(self, error):
        pass

    @abstractmethod
    def raise_invalid_time_exception(self, error):
        pass
    
    @abstractmethod
    def response_for_set_meal_preference(self, meal_request_dto):
        pass
