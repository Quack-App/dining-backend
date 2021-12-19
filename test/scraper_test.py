import app.scraper as scraper
from app.models.resturant import Resturant

from app import scraper

# Ensure that our mock data returns some data
def test_get_soup():
   soup = scraper.get_soup()
   assert soup is not None

# Test to ensure that we can get all 15 resturants
def test_get_resturant():
    soup = scraper.get_soup()
    assert soup is not None
    resturants = scraper.get_resturants(soup)
    assert len(resturants) == 15

def test_scrape_resturant_to_menu():
    resturant = Resturant('DCT', '', '')
    menu = scraper.scrape_resturant_to_menu(resturant)
    assert menu is not None
    assert menu.resturant == resturant
    assert len(menu.food_items) == 5

