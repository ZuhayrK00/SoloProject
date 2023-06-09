class Country:
    def __init__(self, country_name, continent, id = None):
        self.country_name = country_name
        self.continent = continent
        self.id = id

    def country_name(self):
        return self.country_name