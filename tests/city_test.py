import unittest
from models.city import City
from models.country import Country


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city1 = City("Edinburgh", "Scotland")
        self.city2 = City("Barcalona", "Spain")

    def test_city_has_country(self):
        self.assertEqual("Scotland", self.city1.country)

    def test_city_has_name(self):
        self.assertEqual("Barcalona", self.city2.name)
