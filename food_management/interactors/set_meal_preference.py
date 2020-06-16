from datetime import datetime, timedelta

from food_management.interactors.storages.meal_storage_interface\
    import MealStorageInterface
from food_management.interactors.presenters.meal_presenter_interaface\
    import MealPresenterInterface
from food_management.exceptions import\
    InvalidMealIdException,\
    InvalidQuantityException,\
    InvalidItemsException,\
    DuplicateItemsException,\
    InvalidDateTimeException

from food_management.dtos import MealRequestDto

class SetMealPreference:

    def __init__(self,
                 meal_storage: MealStorageInterface
                ):
        self.meal_storage = meal_storage

    def set_meal_preference_wrapper(self,
                                    user_id: int,
                                    meal_request_dto: MealRequestDto,
                                    meal_presenter: MealStorageInterface):
        try:
            response_for_set_meal_preference = self.set_meal_preference(
                user_id,
                meal_request_dto)
        except InvalidMealIdException as error:
            meal_presenter.raise_invalid_meal_id_exception(error)
        except InvalidItemsException as error:
            meal_presenter.raise_invalid_items_exception(error)
        except DuplicateItemsException as error:
            meal_presenter.raise_duplicate_items_exception(error)
        except InvalidQuantityException as error:
            meal_presenter.raise_invalid_quantity_for_items_exception(error)
        except InvalidDateTimeException as error:
            meal_presenter.raise_invalid_time_exception(error)

        response = meal_presenter.response_for_set_meal_preference(
            response_for_set_meal_preference)

        return response

    def set_meal_preference(self,
                            user_id: int,
                            meal_request_dto: MealRequestDto):

        #TODO Meal_id Validation

        meal_id = meal_request_dto.meal_id
        is_meal_id_invalid = not self.meal_storage.validate_meal_id(meal_id)
        if is_meal_id_invalid:
            raise InvalidMealIdException(meal_id)

        #TODO Item_ids_Validation
        items = meal_request_dto.items
        meal_item_ids = self.meal_storage.get_items_of_meal(meal_id)
        invalid_item_ids = []
        for item in items:
            item_id = item.item_id
            is_item_id_invalid = item_id not in meal_item_ids

            if is_item_id_invalid:
                invalid_item_ids.append(item_id)

        is_invalid_items_exist = invalid_item_ids

        if is_invalid_items_exist:
            raise InvalidItemsException(invalid_item_ids)

        #TODO Duplicate_Items_Validation
        items = meal_request_dto.items
        item_ids = [item.item_id for item in items]

        unique_item_ids = set(item_ids)

        for item_id in unique_item_ids:
            item_ids.remove(item_id)

        duplicate_item_ids = list(set(item_ids))
        is_duplicate_items_exist = duplicate_item_ids

        if is_duplicate_items_exist:
            raise DuplicateItemsException(duplicate_item_ids)

        #TODO Quantity_Validation
        item_dtos = meal_request_dto.items
        item_ids = [item.item_id for item in item_dtos]

        items_quantities_dtos = self.meal_storage.get_items_quantities(
            item_ids=item_ids, meal_id=meal_id)

        items_quantities_dtos.sort(key=self.sort_by_item_id)

        invalid_quantity_item_ids = []

        for item_dto, item_quantity_dto in zip(item_dtos,
                                               items_quantities_dtos):
            request_quantity = item_dto.quantity
            is_requested_quantity_negative = not request_quantity < 0
            is_requested_quantity_gt_available = \
                request_quantity > item_quantity_dto.quantity

            is_requested_quantity_invalid = \
                is_requested_quantity_negative or \
                    is_requested_quantity_gt_available

            if is_requested_quantity_invalid:
                invalid_quantity_item_ids.append(item.item_id)

        is_invalid_quantity_items_exist = invalid_quantity_item_ids

        if is_invalid_quantity_items_exist:
            raise InvalidQuantityException(invalid_quantity_item_ids)

        #TODO Date_Validation
        requested_meal_preference_for_date = meal_request_dto.date
        is_time_invalid = not self.meal_storage\
            .validate_meal_preference_date(requested_meal_preference_for_date)
        if is_time_invalid:
            raise InvalidDateTimeException(requested_meal_preference_for_date)

    @staticmethod
    def using_item_id(item_quantity_dto):
        return item_quantity_dto.item_id
