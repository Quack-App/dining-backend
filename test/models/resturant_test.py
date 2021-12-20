from app.models.resturant import Resturant

def test_create_resturant():
    name = "Cafe Name"
    link = "https://testlink.com"
    hours = "8am - 4pm"
    resturant = Resturant(name, link, hours)
    assert name == resturant.name
    assert link == resturant.link
    assert hours == resturant.hours
