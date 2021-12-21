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

    # Create our menu
    restaurant_menu = menu.Menu(restaurant)

    restaurant_html = BeautifulSoup(restaurant_page, 'html.parser')
    # serve_blocks: Breakfast, Lunch, Dinner, etc
    serve_blocks = restaurant_html.select('div.site-panel__daypart-container')
    for serve_block in serve_blocks:
        serve_time_name = serve_block.select('h2.' +
                'panel__title')[0].text.strip()
        serve_time_hours = serve_block.select('div.' +
                'site-panel__daypart-time')[0].text.strip()
        menu_lists = serve_block.select('div.c-tab__content.site-panel__daypart-tab-content')
        # Menu list includes serve specials, condiments, etc
        for menu_list in menu_lists:
            menu_list_inner = menu_list.select('div.c-tab__content-inner')[0]
            menu_list_divs = menu_list_inner.findAll('div', recursive=False)
            # Station blocks don't include all items
            # so we need to iterate over all divs on the same height
            # and also retrieve the divs inside the station block
            station_block = []
            current_station_name = ''
            for div in menu_list_divs:
                if 'station-title-inline-block' in div.attrs['class']:
                    station_name = div.select('h3.site-panel__daypart-station-title')
                    if len(station_name) == 1:
                        station_name = station_name[0].text.strip()
                        if station_name != current_station_name:
                            # We are at a new station
                            items = scrape_station_block(restaurant,
                                    current_station_name, serve_time_name, station_block)
                            restaurant_menu.add_station(serve_time_name,
                                    station_name, items)
                            current_station_name = station_name
                            station_block = div.select('div.site-panel__daypart-item')
                if 'site-panel__daypart-item' in div.attrs['class']:
                    station_block.append(div)

    return restaurant_menu

def scrape_station_block(restaurant: restaurant.Restaurant,
        station_name: str, serve_time: str, station_block: list) -> list:
    '''
    Scrape a station block (divs surrounded by stations)
    and returns a list of food items
    '''
    if station_name == '':
        return []

    food_items = []
    for div in station_block:
        name = div.select('button.h4')[0].text.strip()
        calories = div.find('div',
                attrs={'class': 'site-panel__daypart-item-calories'}).text.strip()
        categories = [] # TODO: Get categories
        food_items.append(food_item.FoodItem(
            restaurant, serve_time, station_name, name, calories, categories))

    return food_items


if __name__ == '__main__':
    s = get_soup()
    r = get_restaurants(s)
    print(r)
