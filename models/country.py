class Country:

    def __init__(self, name, continent, language, visited = False, id = None):
            self.name = name
            self.continent = continent
            self.language = language
            self.visited = visited
            self.id = id

    def has_visited(self):
        self.visted = True