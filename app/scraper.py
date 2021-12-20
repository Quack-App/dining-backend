'''Implements scraper functionality to get Bon Appetit Data as Models'''
import requests
from bs4 import BeautifulSoup
from app.models import restaurant
from app.models import menu
from app.models import food_item

import sys

# Bon Appetit Website Base URL
BASE_URL =  'https://emoryatlanta.cafebonappetit.com'

def get_soup():
    '''
    Get scrapped data if it is not a test
    '''
    if 'pytest' not in sys.modules:
        html = requests.get(BASE_URL)
        if html.status_code != 200:
            raise Exception(f'[Scraper.py] Invalid status \
                    code {html.status_code} for BASE_URL: {BASE_URL}')
        soup = BeautifulSoup(html.content, 'html.parser')
        return soup

    # Use saved HTML mocked data instead
    # If this fails, ensure you are running `pytest`
    # from the root project folder
    with open('./data/root.html', 'r', encoding='utf-8') as file:
        contents = file.read()
        soup = BeautifulSoup(contents, 'html.parser')
        return soup

def get_restaurants(soup: BeautifulSoup):
    '''
    Get all restaurants listed on the Bon Appetit Website,
    their hours, and crawl URL's
    '''
    restaurants_html = soup.findAll('div',
            attrs = {'class': 'c-accordion__row site-panel__cafeinfo-row'})
    restaurants = []
    for restaurant_html in restaurants_html:
        name = restaurant_html.find('span',
                attrs = {'class': 'c-accordion__header-inner ' +
                        'site-panel__cafeinfo-row-header-inner'}).text.strip()
        link = restaurant_html.find('a',
                attrs = {'class': 'site-panel__cafeinfo-view-more'})['href']
        hours = restaurant_html.find('span',
                attrs = {'class' : 'site-panel__cafeinfo-header-extra'}).text.strip()

        restaurants.append(restaurant.Restaurant(name, link, hours))

    return restaurants

def scrape_restaurant_to_menu(restaurant: restaurant.Restaurant) -> menu.Menu:
    '''
    Scrape a restaurant and convert data to Menu object
    '''
    if "pytest" not in sys.modules:
        restaurant_page = requests.get(restaurant.link)
    else:
        with open('./data/dct.html', 'r', encoding='utf-8') as html:
            restaurant_page = html.read()
    restaurant_html = BeautifulSoup(restaurant_page, 'html.parser')
    # Finds serve times -- CSS is consistent across different Cafe's
    # TODO: Get serve times
    # TODO: Get current serve time
    # TODO: Get serve names
    # TODO: Get current serve name
    # TODO: Refactor app.models.restaurant to seperate by serve time
    serve_blocks = restaurant_html.select('section.panel.s-wrapper.site-panel.site-panel--daypart')
    for serve_block in serve_blocks:
        # TODO: Get food items from restaurant here!
        pass
    food_items = serve_blocks
    
    # Return empty list of food_items if no menu at this time
    return menu.Menu(restaurant, food_items)


if __name__ == '__main__':
    s = get_soup()
    r = get_restaurants(s)
    print(r)
