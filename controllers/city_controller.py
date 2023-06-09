from flask import Flask, render_template, request, redirect, Blueprint
from models.city import City
from models.country import Country
import repository.city_repository as city_repository
import repository.country_repository as country_repository

cities_blueprint = Blueprint('cities', __name__)

@cities_blueprint.route('/cities')
def cities():
    cities = city_repository.select_all()
    return render_template('cities/index.html', all_cities=cities)

# New
@cities_blueprint.route('/cities/new.html', methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template('cities/new.html', all_countries=countries)

# Create
@cities_blueprint.route('/cities', methods=['POST'])
def create_city():
    city_name = request.form['city_name']
    visited = request.form['visited']
    country = country_repository.select(request.form['country_id'])
    city = City(city_name, visited, country)
    city_repository.save(city)
    return redirect('/cities')

# Show
@cities_blueprint.route('/cities/<iid>', methods=['GET'])
def show_city(id):
    city = city_repository.select(id)
    return render_template('cities/show.html', city=city)

# Edit
@cities_blueprint.route('/cities/<id>/edit', methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template('cities/edit.html', city=city, all_countries=countries)

# Update
@cities_blueprint.route('/cities/<id>', methods=['PUT'])
def update_city(id):
    city_name = request.form['city_name']
    visited = request.form['visited']
    country = country_repository.select(request.form['country_id'])

    city = City(city_name, visited, country, id)
    city_repository.update(city)
    return redirect('/cities')

# Delete
@cities_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/books')

@cities_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/books')

# Create
@cities_blueprint.route('/countries/new', methods=['GET', 'POST'])
def create_country():
    if request.method == 'POST':
        country_name = request.form['country_name']
        new_country = Country(country_name)
        country_repository.save(new_country)
        return redirect('/countries')
    # return render_template('books/create_author.html', author = None)
    