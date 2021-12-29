"""
Implements the Menu class which stores restaurant
and food item data
"""

from .restaurant import Restaurant
from .food_item import FoodItem


class Menu:
    """
    Stores the restaurant and food item data
    """

    def __init__(self, restaurant: Restaurant):
        """
        self.menu: dict[str, str]
        -- structure:
            Serve Block (Breakfast, Lunch)
                - Station (Breakfast Grill, Grill)
                    - Food Item (Fries)
        """
        self.restaurant = restaurant
        self.menu = {}

    def add_station(
        self, serve_block: str, station_name: str, food_items: list
    ) -> bool:
        if serve_block not in self.menu.keys():
            # Set empty block
            self.menu[serve_block] = {}

        if station_name == "":
            if len(food_items) > 0:
                raise Exception(f"Tried to create empty station name with {len(food_items)} food items")
            else:
                return False

        if station_name not in self.menu[serve_block]:
            # Add station to serve block
            self.menu[serve_block][station_name] = []

        ok = True
        for item in food_items:
            ok = ok and self.add_food_item(serve_block, item)

        return ok

    def add_food_item(self, serve_block: str, item: FoodItem) -> bool:
        """
        add_food_item adds a FoodItem to the list of foods for a station
        serve_block: str
            - Breakfast, Dinner, etc
        returns true if the item is unique and added successfully
        """
        if item is None:
            raise Exception("[menu#add_food_item] Tried to add None food item")
        if not isinstance(item, FoodItem):
            raise Exception(
                "[menu#add_food_item] Tried to add item of type not FoodItem"
            )
        if item.station not in self.menu[serve_block]:
            raise Exception(
                "[menu#add_food_item] tried to add FoodItem to station that does not exist"
            )
        for food_item in self.menu[serve_block][item.station]:
            if food_item.name == item.name:
                print(f"[menu#add_food_item] skipping duplicate item {item}")
                return False

        self.menu[serve_block][item.station].append(item)
        return True

    def to_json(self) -> dict[str, dict]:
        """
        Serialize the object to JSON
        """
        return {"restaurant": self.restaurant.to_json(),
                "menu": self.menu}
