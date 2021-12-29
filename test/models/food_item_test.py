from app.models.food_item import FoodItem
from app.models.restaurant import Restaurant

def test_food_item_create():
    restaurant = Restaurant('', '', '')
    serve_time = ''
    station = "Station"
    name = "Name"
    calories = 40
    categories = ["Category 1"]
    food_item = FoodItem(restaurant, serve_time, station, name, calories, categories)

    assert station == food_item.station
    assert name == food_item.name
    assert calories == food_item.calories
    assert categories == food_item.categories
