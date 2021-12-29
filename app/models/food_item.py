from .restaurant import Restaurant

"""
FoodItem stores all food item related data
such as station, name, calories, categories, etc.
"""


class FoodItem:
    def __init__(
        self,
        restaurant: Restaurant,
        serve_time: str,
        station: str,
        name: str,
        calories: int,
        categories: list,
    ):
        self.restaurant = restaurant
        self.serve_time = serve_time
        self.station = station
        self.name = name
        self.calories = calories
        self.categories = categories

    def __str__(self):
        return f"{self.station}, {self.name}"

    def __repr__(self):
        return f"{self.restaurant.name}, {self.station}, {self.name}"

    def to_json(self):
        return {
            "restaurant": self.restaurant.to_json(),
            "serve_time": self.serve_time,
            "station": self.station,
            "name": self.name,
            "calories": self.calories,
        }
