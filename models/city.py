class City:
    def __init__(self, name, country, visited=False, id=None):
        self.name = name
        self.country = country
        self.visited = visited
        self.id = id

    def has_visited(self):
        self.visited = True
