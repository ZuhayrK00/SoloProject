from flask import Flask, render_template
from flask import Flask, render_template_string

from controllers.cities_controller import cities_blueprint
from controllers.countries_controller import countries_blueprint
from controllers.bucketlist_controller import bucketlist_blueprint
from controllers.completed_controller import completed_blueprint

app = Flask(__name__)

app.register_blueprint(cities_blueprint)
app.register_blueprint(countries_blueprint)
app.register_blueprint(bucketlist_blueprint)
app.register_blueprint(completed_blueprint)


@app.route("/")
def main():
    return render_template("home.html")

@app.route("/index")
def base():
    return render_template("index.html")

if __name__ == "__main__":
    app.run
