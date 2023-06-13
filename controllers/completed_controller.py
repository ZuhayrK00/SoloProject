from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

bucketlist_blueprint = Blueprint("bucketlist", __name__)


@bucketlist_blueprint.route("/bucketlist")
def bucketlist():

    completed_cities = [city for city in city_repository.select_all() if city.visited is True]

    countries = country_repository.select_all()
    completed_countries = []
    for country in countries:
        if country.visited is True:
            completed_countries.append(country)

    return render_template("/completed.html", all_cities=completed_cities, all_countries = completed_countries)