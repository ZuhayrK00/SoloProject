from db.run_sql import run_sql
from models.city import City
from models.country import Country
import repository.country_repository as country_repository

def save(city):
    sql = "INSERT INTO cities (city_name, visited, country_id) VALUES (%s, %s, %s) RETURNING *"
    values = (city.name, city.visited, city.country_id)
    result = run_sql(sql, values)
    id = result[0]['id']
    city.id = id
    return city

