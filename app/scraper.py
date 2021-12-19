'''Implements scraper functionality to get Bon Appetit Data as Models'''
import requests
from bs4 import BeautifulSoup
from app.models import resturant
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

def get_resturants(soup: BeautifulSoup):
    '''
    Get all resturants listed on the Bon Appetit Website,
    their hours, and crawl URL's
    '''
    resturants_html = soup.findAll('div',
            attrs = {'class': 'c-accordion__row site-panel__cafeinfo-row'})
    resturants = []
    for resturant_html in resturants_html:
        name = resturant_html.find('span',
                attrs = {'class': 'c-accordion__header-inner ' +
                        'site-panel__cafeinfo-row-header-inner'}).text.strip()
        link = resturant_html.find('a',
                attrs = {'class': 'site-panel__cafeinfo-view-more'})['href']
        hours = resturant_html.find('span',
                attrs = {'class' : 'site-panel__cafeinfo-header-extra'}).text.strip()

        resturants.append(resturant.Resturant(name, link, hours))

    return resturants

def scrape_resturant_to_menu(resturant: resturant.Resturant) -> menu.Menu:
    '''
    Scrape a resturant and convert data to Menu object
    '''
    if "pytest" not in sys.modules:
        resturant_page = requests.get(resturant.link)
    else:
        with open('./data/dct.html', 'r', encoding='utf-8') as html:
            resturant_page = html.read()
    resturant_html = BeautifulSoup(resturant_page, 'html.parser')
    # Finds serve times -- CSS is consistent across different Cafe's
    # TODO: Get serve time
    # TODO: Get serve name
    # TODO: Refactor app.models.resturant to seperate by serve time
    serve_blocks = resturant_html.select('section.panel.s-wrapper.site-panel.site-panel--daypart')
    for serve_block in serve_blocks:
        

    food_items = serve_times
    # TODO: Get food items from resturant here!
    # Return empty list of food_items if no menu at this time
    return menu.Menu(resturant, food_items)


if __name__ == '__main__':
    s = get_soup()
    r = get_resturants(s)
    print(r)
