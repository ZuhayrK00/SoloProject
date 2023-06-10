import pdb
from models.city import City
from models.country import Country
import repository.city_repository as city_repository
import repository.country_repository as country_repository

city_repository.delete_all()
country_repository.delete_all()

country1 = ("Spain", "Europe")
country_repository.save(country1)
country2 = ("France", "Europe")
country_repository.save(country2)

city1 = ("Paris", country2, True)
city_repository.save(city1)
city2 = ("Madrid", country1, False)
city_repository.save(city2)