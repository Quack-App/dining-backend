'''
Implements the Menu class which stores restaurant
and food item data
'''

from .restaurant import Restaurant
from .food_item import FoodItem


class Menu:
    '''
    Stores the restaurant and food item data
    '''
    def __init__(self, restaurant: Restaurant, food_items: list = None):
        self.restaurant = restaurant
        self.food_items = food_items
        if self.food_items is None:
            self.food_items = []

    def add_food_item(self, item: FoodItem) -> bool:
        '''
        add_food_item adds a FoodItem to the list of
        returns true if the item is unique and added successfully
        '''
        if item is None:
            raise Exception('[menu#add_food_item] Tried to add None food item')
        if not isinstance(item, FoodItem):
            raise Exception('[menu#add_food_item] Tried to add item of type not FoodItem')
        for food_item in self.food_items:
            if food_item.name == item.name and \
                    food_item.station == item.station:
                print(f'[menu#add_food_item] skipping duplicate item {item}')
                return False

        self.food_items.append(item)
        return True
