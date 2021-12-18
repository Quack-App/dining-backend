import app.scraper as scraper
from app import scraper

# Ensure that our mock data returns some data
def test_get_soup():
   soup = scraper.get_soup(is_test=True)
   assert soup is not None

soup = scraper.get_soup(is_test=True)

# Test to ensure that we can get all 15 resturants
def test_get_resturant():
    assert soup is not None
    resturants = scraper.get_resturants(soup)
    assert len(resturants) == 15
