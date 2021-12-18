'''Implements scraper functionality to get Bon Appetit Data as Models'''
import requests
from bs4 import BeautifulSoup
from app.models import resturant

# Bon Appetit Website Base URL
BASE_URL =  'https://emoryatlanta.cafebonappetit.com'

def get_soup(is_test = False):
    '''
        Get scrapped data if it is not a test
    '''
    if not is_test:
        html = requests.get(BASE_URL)
        if html.status_code != 200:
            raise Exception(f'[Scraper.py] Invalid status code {html.status_code} for ROOT_URL: {ROOT_URL}')
        soup = BeautifulSoup(html.content, 'html.parser')
        return soup

    # Use saved HTML mocked data instead
    # If this fails, ensure you are running `pytest`
    # from the root project folder
    with open('./data/root.html', 'r', encoding='utf-8') as file:
        contents = file.read()
        soup = BeautifulSoup(contents, 'html.parser')
        return soup

def get_resturants(soup=BeautifulSoup):
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


if __name__ == '__main__':
    s = get_soup()
    r = get_resturants(s)
    print(r)
