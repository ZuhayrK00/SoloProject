import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository


city_repository.delete_all()
country_repository.delete_all()

country1 = Country('Spain', 'Europe', 'Spanish')
country_repository.save(country1)
country2 = Country('Scotland', 'Europe', 'English')
country_repository.save(country2)
country3 = Country('Usa', 'North America', 'English')
country_repository.save(country3)
country4 = Country('Italy', 'Europe', 'Italian')
country_repository.save(country4)


city1 = City('Edinburgh', country2)
city_repository.save(city1)
city2 = City('Barcelona', country1)
city_repository.save(city2)
city7 = City('New York', country3)
city_repository.save(city7)
city8 = City('Munich', country4)
city_repository.save(city8)


