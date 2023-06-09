from flask import Flask, render_template

from controllers.city_controller import city_controller

app = Flask(__name__)

app.register_blueprint(cities_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)