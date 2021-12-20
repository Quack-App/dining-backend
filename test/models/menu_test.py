from app.models.menu import Menu
from app.models.resturant import Resturant
from app.models.food_item import FoodItem
import pytest

def test_menu_create():
    r_name = 'Name'
    r_link = 'https://testlink.com'
    r_hours = '8am - 4pm'
    resturant = Resturant(r_name, r_link, r_hours)
    menu = Menu(resturant)
    assert menu.resturant == resturant
    assert menu.food_items == []

def test_add_food_item():
    r_name = 'Name'
    r_link = 'https://testlink.com'
    r_hours = '8am - 4pm'
    resturant = Resturant(r_name, r_link, r_hours)
    menu = Menu(resturant)
    f_station = 'Station'
    f_name = 'Name'
    f_calories = 40
    f_categories = ['Category 1']
    food_item = FoodItem(f_station, f_name, f_calories, f_categories)
    menu.add_food_item(food_item)
    assert len(menu.food_items) == 1
    assert menu.food_items[0].__str__() == food_item.__str__()

def test_add_food_item_none():
    r_name = 'Name'
    r_link = 'https://testlink.com'
    r_hours = '8am - 4pm'
    resturant = Resturant(r_name, r_link, r_hours)
    menu = Menu(resturant)
    with pytest.raises(Exception):
        menu.add_food_item(None)
