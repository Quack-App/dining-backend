from fastapi import FastAPI, Response, status
from fastapi_utils.tasks import repeat_every
from starlette.responses import RedirectResponse
from . import scraper

app = FastAPI()

menus = []


@app.get("/")
def root():
    response = RedirectResponse(url="/docs")
    return response


@app.get("/get_data")
def get_data(response: Response):
    response.status_code = status.HTTP_200_OK
    return {"menus": [menu.to_json() for menu in menus]}


@app.on_event("startup")
@repeat_every(seconds=60 * 60)  # Repeat every hour
@app.post("/scrape_data")
def scrape_data():
    """
    Update menus by rescraping data - runtime cache
    """
    global menus
    soup = scraper.get_soup()
    restaurants = scraper.get_restaurants(soup)
    menus = []
    for restaurant in restaurants:
        menus.append(scraper.scrape_restaurant_to_menu(restaurant))
    return {"msg" : "Finished scraping data"}
