import unittest
from models.country import Country


class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country1 = Country("Scotland", "Europe", "English")
        self.country2 = Country("Spain", "Europe", "Spanish")

    def test_country_has_name(self):
        self.assertEqual("Scotland", self.country1.name)

    def test_country_has_language(self):
        self.assertEqual("English", self.country1.language)

    def test_country_has_continent(self):
        self.assertEqual("Europe", self.country2.continent)
