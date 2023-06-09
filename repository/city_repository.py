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

def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    result = run_sql(sql)

    for row in result:
        country = country_repository.select(row['country_id'])
        city = City(row['city_name'], row['visited'], country, row['id'])
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        country = country_repository.select(result['country_id'])
        city = City(result['city_name'], result['visited'], country, result['id'])
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(city):
    sql = "UPDATE citities SET (city_name, visited, country_id) = (%s, %s, %s) WHERE id = %s"
    values = (city.name, city.visited, city.country_id, city.id)
    print(values)
    run_sql(sql, values)
    