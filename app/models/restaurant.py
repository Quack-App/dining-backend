class Restaurant:
    def __init__(self, name: str, link: str, hours: str):
        self.name = name
        self.link = link
        self.hours = hours

    def __str__(self):
        return f"{self.name}, {self.hours}, {self.link}"

    def __repr__(self):
        return f"<Restaurant: {self.name}, {self.hours}, {self.link}>"

    def to_json(self):
        return {"name": self.name, "link": self.link, "hours": self.hours}
