import app.scraper as scraper
from app.models.restaurant import Restaurant

from app import scraper

# Ensure that our mock data returns some data
def test_get_soup():
    soup = scraper.get_soup()
    assert soup is not None


# Test to ensure that we can get all 15 restaurants
def test_get_restaurant():
    soup = scraper.get_soup()
    assert soup is not None
    restaurants = scraper.get_restaurants(soup)
    assert len(restaurants) == 15


def test_scrape_restaurant_to_menu():
    restaurant = Restaurant("DCT", "", "")
    menu = scraper.scrape_restaurant_to_menu(restaurant)
    assert menu is not None
    assert menu.restaurant == restaurant
    assert menu.menu != {}
    assert len(menu.menu.keys()) == 5
    assert len(menu.menu["Breakfast"].keys()) == 10
    assert len(menu.menu["Breakfast"]["breakfast"]) == 6
