from app.models.restaurant import Restaurant

def test_create_restaurant():
    name = "Cafe Name"
    link = "https://testlink.com"
    hours = "8am - 4pm"
    restaurant = Restaurant(name, link, hours)
    assert name == restaurant.name
    assert link == restaurant.link
    assert hours == restaurant.hours
