'''
FoodItem stores all food item related data
such as station, name, calories, categories, etc.
'''
class FoodItem:
    def __init__(self, station: str, name: str, calories: int, categories: list):
        self.station = station
        self.name = name
        self.calories = calories
        self.categories = categories

    def __str__(self):
        return f'{self.station}, {self.name}'

    def __repr__(self):
        return f'{self.station}, {self.name}'
