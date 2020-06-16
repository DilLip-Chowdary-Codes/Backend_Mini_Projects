class InvalidQuantityException(Exception):
    def __init__(self, quantity):
        self.quantity = quantity

class InvalidItemsException(Exception):
    def __init__(self, item_ids):
        self.item_ids = item_ids

class InvalidMealIdException(Exception):
    def __init__(self, meal_id):
        self.meal_id = meal_id

class DuplicateItemsException(Exception):
    def __init__(self, item_ids):
        self.item_ids = item_ids

class InvalidDateTimeException(Exception):
    def __init__(self, set_meal_preference_for_date):
        self.set_preference_for_date = set_meal_preference_for_date
