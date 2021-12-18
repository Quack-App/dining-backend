class Resturant:
    def __init__(self, name: str, link: str, hours: str):
        self.name = name
        self.link = link
        self.hours = hours

    def __str__(self):
        return f'{self.name}, {self.hours}, {self.link}'

    def __repr__(self):
        return f'<Resturant: {self.name}, {self.hours}, {self.link}>'
