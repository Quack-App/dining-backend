from app.models.menu import Menu
from app.models.restaurant import Restaurant
from app.models.food_item import FoodItem
import pytest

def test_menu_create():
    r_name = 'Name'
    r_link = 'https://testlink.com'
    r_hours = '8am - 4pm'
    restaurant = Restaurant(r_name, r_link, r_hours)
    menu = Menu(restaurant)
    assert menu.restaurant == restaurant
    assert menu.food_items == []

def test_add_food_item():
    r_name = 'Name'
    r_link = 'https://testlink.com'
    r_hours = '8am - 4pm'
    restaurant = Restaurant(r_name, r_link, r_hours)
    menu = Menu(restaurant)
    f_station = 'Station'
    f_name = 'Name'
    f_serve_time = 'Breakfast'
    f_calories = 40
    f_categories = ['Category 1']
    food_item = FoodItem(restaurant, f_serve_time, f_station, f_name, f_calories, f_categories)
    menu.add_food_item(food_item)
    assert len(menu.food_items) == 1
    assert menu.food_items[0].__str__() == food_item.__str__()

def test_add_food_item_none():
    r_name = 'Name'
    r_link = 'https://testlink.com'
    r_hours = '8am - 4pm'
    restaurant = Restaurant(r_name, r_link, r_hours)
    menu = Menu(restaurant)
    with pytest.raises(Exception):
        menu.add_food_item(None)
