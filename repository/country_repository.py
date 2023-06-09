from flask import render_template, request, redirect
from db.run_sql import run_sql
from models.country import Country
import repository.country_repository as country_repository

def save(country):
    sql = "INSERT INTO country (country_name, continent) VALUES (%s, %s) RETURNING *"
    values = (country.country_name, country.continent)
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['country_name'], row['continent'], row['id'])
        countries.append(country)
    return countries
