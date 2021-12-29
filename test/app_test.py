from fastapi.testclient import TestClient
from app import app

client = TestClient(app.app)

def test_home():
    response = client.get("/")
    assert response.url.endswith("/docs")

def test_scrape_data():
    response = client.post("/scrape_data")
    assert "msg" in response.json()

def test_get_data():
    response = client.get("/get_data")
    assert response.json() is not None
    assert "menus" in response.json()
    # 15 different eating options
    assert len(response.json()["menus"]) == 15
    dct_data = response.json()["menus"][0]
    # {menu: ..., restaurant: ...}
    assert len(dct_data) == 2
    # Breakfast, Lunch, Late Lunch, Dinner, Late Dinner
    assert len(dct_data["menu"]) == 5
    assert len(dct_data["menu"]["Breakfast"]) == 10
    assert len(dct_data["menu"]["Lunch"]) == 17
    assert len(dct_data["menu"]["Late Lunch"]) == 3
    assert len(dct_data["menu"]["Dinner"]) == 8
    assert len(dct_data["menu"]["Dinner"]["605 kitchen"]) == 1
    assert len(dct_data["menu"]["Late Night"]) == 3
