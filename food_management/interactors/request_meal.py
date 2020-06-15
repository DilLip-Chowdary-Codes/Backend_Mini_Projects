from food_management.dtos import MealRequestDto
from food_management.interactors.storages.meal_storage_interface\
    import MealStorageInterface
from food_management.interactors.presenters.meal_presenter_interaface\
    import MealPresenterInterface
from datetime import datetime, timedelta

class MealRequest:
    
    def __init__(self,
                 meal_storage: MealStorageInterface
                ):
        self.meal_storage = meal_storage
    
    def meal_request(self, meal_request_dto: MealRequestDto):


        #TODO Meal_Validation
        
        #TODO Meal_Type_Validation
        #TODO Quantity_Validation
        #TODO Item_Validation
        #TODO Duplicate_Items_Validation

        #TODO Date_Validation
        # requested_time = datetime.now()
        # is_time_exceeded = ""
        pass