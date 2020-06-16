import pytest
from freezegun import freeze_time
from datetime import datetime
from food_management.dtos import \
    MealRequestDto, ItemDto

@pytest.fixture()
def Items():
    items_list = [
        ItemDto(item_id=num,quantity=2)
        for num in range(5)
        ]
    return items_list

@pytest.fixture()
def item_quantity_dtos():
    items_list = [
        ItemDto(item_id=num,quantity=2)
        for num in range(5)
        ]

    item_invalid_quantity = ItemDto(
        item_id=3,quantity=100)
    items_list.append(item_invalid_quantity)

    return items_list

@pytest.fixture()
def meal_request_dto_with_invalid_meal_id(Items):
    with freeze_time("2020-06-15"):
        meal_request_dto = MealRequestDto(
            meal_id=1,
            items=Items,
            date=datetime.now())
    return meal_request_dto

@pytest.fixture()
def meal_request_dto_with_invalid_items(Items):

    with freeze_time("2020-06-15"):
        meal_request_dto = MealRequestDto(
            meal_id=1,
            items=Items,
            date=datetime.now())

    return meal_request_dto

@pytest.fixture()
def meal_request_dto_with_duplicate_items(Items):
    items = Items
    duplicate_items =[Items[0], Items[1]]
    items = items + duplicate_items

    with freeze_time("2020-06-15"):
        meal_request_dto = MealRequestDto(
            meal_id=1,
            items=items,
            date=datetime.now())

    return meal_request_dto

@pytest.fixture
def meal_request_dto_with_invalid_quantity_items(item_quantity_dtos):

    Items = item_quantity_dtos
    items = Items
    item_with_invalid_quantity = [
        ItemDto(item_id=5,
                quantity=5)
        ]

    items = items + item_with_invalid_quantity

    with freeze_time("2020-06-15"):
        meal_request_dto = MealRequestDto(
            meal_id=1,
            items=items,
            date=datetime.now())

    return meal_request_dto

# @pytest.fixture
# def item_quantity_dtos():
#     item_quantity_dtos_list = [
#         ItemQuantityDto(item_id=num,
#                         quantity=2)
#                         for num in range(5)
#                         ]
#     return item_quantity_dtos_list


# @pytest.fixture
# def item_quantity_dtos_with_invalid_quantity(item_quantity_dtos):
#     item_quantity_dtos_list = item_quantity_dtos
#     invalid_quantityitemItemQuantityDto
#     item_quantity_dtos_list.append()
#     return item_quantity_dtos_list


