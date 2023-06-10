from db.run_sql import run_sql

from models.country import Country
from models.city import City


def save(country):
    sql = "INSERT INTO countries (name, continent, language, visited) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [country.name, country.continent, country.language, country.visited]
    results = run_sql(sql, values)
    id = results[0]["id"]
    country.id = id
    return country


def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(
            row["name"], row["continent"], row["language"], row["visited"], row["id"]
        )
        countries.append(country)
    return countries


def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(
            result["name"],
            result["continent"],
            result["language"],
            result["visited"],
            result["id"],
        )
    return country


def delete_all():
    sql = "DELETE  FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(country):
    sql = "UPDATE countries SET (name, continent, language, visited) = (%s, %s, %s, %s) WHERE id = %s"
    values = [
        country.name,
        country.continent,
        country.language,
        country.visited,
        country.id,
    ]
    run_sql(sql, values)
from db.run_sql import run_sql

from models.country import Country
from models.city import City

def save(country):
    sql = "INSERT INTO countries (name, continent, language, visited) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [country.name, country.continent, country.language, country.visited]
    results = run_sql(sql, values)
    id = results[0]["id"]
    country.id = id
    return country

def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(
            row["name"], row["continent"], row["language"], row["visited"], row["id"]
        )
        countries.append(country)
    return countries