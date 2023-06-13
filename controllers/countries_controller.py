from db.run_sql import run_sql
from flask import Blueprint, Flask, redirect, render_template, request

from models.country import Country

from repositories import country_repository

countries_blueprint = Blueprint("countries", __name__)


# INDEX
@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries=countries)


# NEW
@countries_blueprint.route("/countries/new")
def new_country():
    new_country = country_repository.select_all()
    return render_template("/countries/new.html", country=new_country)


# CREATE
@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    name = request.form["name"]
    continent = request.form["continent"]
    language = request.form["language"]
    # visited = request.form['visited']
    country = Country(name, continent, language)
    country_repository.save(country)
    return redirect("/countries")


# SHOW
@countries_blueprint.route("/countries/<id>", methods=["GET"])
def show_country(id):
    country = country_repository.select(id)
    return render_template("countries/show.html", country=country)


# EDIT
@countries_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    country = country_repository.select(id)
    return render_template("countries/edit.html", country=country)


# UPDATE
@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    name = request.form["name"]
    continent = request.form["continent"]
    language = request.form["language"]
    visited = request.form["visited"]
    country = Country(name, continent, language, visited, id)
    country_repository.update(country)
    return redirect("/countries")


# DELETE
def delete_all(id):
    sql = "DELETE  FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# DELETE ONE
@countries_blueprint.route("/countries/<id>/delete", methods=["POST"])
def delete(id):
    country_repository.delete(id)
    return redirect("/countries")


# MARK VISITED
@countries_blueprint.route("/countries/<id>/mark_visited", methods=["POST"])
def mark_country_visited(id):
    country = country_repository.select(id)
    country.visited = True  # Set visited as True
    country_repository.update(country)
    return redirect("/bucketlist")


# GALLERY
@countries_blueprint.route("/countries/<id>/gallery", methods=["GET"])
def show_gallery(id):
    country = country_repository.select(id)
    return render_template(
        "countries/gallery.html", country=country, country_name=country.name
    )

# NOT VISITED
@countries_blueprint.route("/countries/<id>/not_visited", methods=["POST"])
def not_visited(id):
    country = country_repository.select(id)
    country.visited = False  # Set visited as True
    country_repository.update(country)
    return redirect("/completed")
