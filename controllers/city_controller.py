from flask import Flask, render_template, request, redirect, Blueprint
from models.city import City
from models.country import Country
import repository.city_repository as city_repository
import repository.country_repository as country_repository

cities_blueprint = Blueprint('cities', __name__)