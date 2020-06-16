import pytest
from unittest.mock import Mock, create_autospec
from django_swagger_utils.drf_server.exceptions\
    import BadRequest
from food_management.interactors.storages.meal_storage_interface\
    import MealStorageInterface
from food_management.interactors.presenters.meal_presenter_interaface\
    import MealPresenterInterface
from food_management.interactors.set_meal_preference\
    import SetMealPreference
from food_management.exceptions import InvalidMealIdException

class TestSetMealPreference:

    def test_set_meal_preference_with_invalid_meal_id_raises_exception(
        self,
        meal_request_dto_with_invalid_meal_id):

        #arrange
        user_id = 1
        meal_request_dto = meal_request_dto_with_invalid_meal_id
        meal_storage = create_autospec(MealStorageInterface)
        meal_presenter = create_autospec(MealPresenterInterface)
        interactor = SetMealPreference(meal_storage=meal_storage)
        meal_storage.validate_meal_id.return_value = False
        meal_presenter.raise_invalid_meal_id_exception\
            .side_effect = BadRequest
        expected_call_object_attribute = 1
        expected_call_type = InvalidMealIdException

        #act
        with pytest.raises(BadRequest):
            interactor.set_meal_preference_wrapper(
                user_id=user_id,
                meal_request_dto=meal_request_dto,
                meal_presenter=meal_presenter)

        #assert
        call_object = meal_presenter.raise_invalid_meal_id_exception\
            .call_args
        call_args=call_object.args

        call_argument =call_args[0]

        call_object_attribute = call_argument.meal_id
        call_type = type(call_argument)
        meal_storage.validate_meal_id.assert_called_once_with(
            meal_request_dto.meal_id)
        assert call_object_attribute == expected_call_object_attribute
        assert call_type == expected_call_type

    def test_set_meal_preference_with_invalid_items_raises_exception(
        self,
        meal_request_dto_with_invalid_items):

        #arrange
        user_id = 1
        meal_item_ids = [1,2,3,4,5,6,7,8]
        meal_request_dto = meal_request_dto_with_invalid_items
        meal_storage = create_autospec(MealStorageInterface)
        meal_presenter = create_autospec(MealPresenterInterface)
        interactor = SetMealPreference(meal_storage=meal_storage)
        meal_storage.validate_meal_id.return_value = True
        meal_storage.get_items_of_meal.return_value = meal_item_ids
        meal_presenter.raise_invalid_items_exception\
            .side_effect = BadRequest

        #act
        with pytest.raises(BadRequest):
            interactor.set_meal_preference_wrapper(
                user_id=user_id,
                meal_request_dto=meal_request_dto,
                meal_presenter=meal_presenter)

        #assert
        meal_storage.validate_meal_id.assert_called_once_with(
            meal_request_dto.meal_id)
        meal_storage.get_items_of_meal.assert_called_once_with(
            meal_request_dto.meal_id)

    def test_set_meal_preference_with_duplicate_items_raises_exception(
        self,
        meal_request_dto_with_duplicate_items):

        #arrange
        user_id = 1
        meal_item_ids = [1,2,3,4,5]
        meal_request_dto = meal_request_dto_with_duplicate_items
        meal_storage = create_autospec(MealStorageInterface)
        meal_presenter = create_autospec(MealPresenterInterface)
        interactor = SetMealPreference(meal_storage=meal_storage)
        meal_storage.validate_meal_id.return_value = True
        meal_storage.get_items_of_meal.return_value = meal_item_ids
        meal_presenter.raise_invalid_items_exception\
            .side_effect = BadRequest

        #act
        with pytest.raises(BadRequest):
            interactor.set_meal_preference_wrapper(
                user_id=user_id,
                meal_request_dto=meal_request_dto,
                meal_presenter=meal_presenter)

        #assert
        meal_storage.validate_meal_id.assert_called_once_with(
            meal_request_dto.meal_id)
        meal_storage.get_items_of_meal.assert_called_once_with(
            meal_request_dto.meal_id)

    def test_set_meal_preference_with_invalid_quantity_raises_exception(
        self,
        meal_request_dto_with_invalid_quantity_items,
        item_quantity_dtos):

        #arrange
        user_id = 1
        meal_item_ids = [0, 1, 2, 3, 4, 5]
        meal_request_dto = meal_request_dto_with_invalid_quantity_items
        meal_storage = create_autospec(MealStorageInterface)
        meal_presenter = create_autospec(MealPresenterInterface)
        interactor = SetMealPreference(meal_storage=meal_storage)
        meal_storage.validate_meal_id.return_value = True
        meal_storage.get_items_of_meal.return_value = meal_item_ids
        meal_storage.get_items_quantities.return_value = item_quantity_dtos
        meal_presenter.raise_invalid_quantity_for_items_exception\
            .side_effect = BadRequest

        #act
        with pytest.raises(BadRequest):
            interactor.set_meal_preference_wrapper(
                user_id=user_id,
                meal_request_dto=meal_request_dto,
                meal_presenter=meal_presenter)

        #assert
        meal_storage.validate_meal_id.assert_called_once_with(
            meal_request_dto.meal_id)
        meal_storage.get_items_of_meal.assert_called_once_with(
            meal_request_dto.meal_id)
        # (item_ids=item_ids, meal_id=meal_id)

