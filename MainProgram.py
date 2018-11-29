from flask import Flask, render_template, request 
from location import *
from places import *
from settings import KEYS


app = Flask("MyApp")

@app.route("/")
def display_location():
    
    return render_template("IOCategories.html", location = my_city(), OpenWeatherMap_API_KEY = KEYS['OpenWeatherMap'], all_places_display_name = all_places_names.values())


if __name__ == '__main__':
    app.run(debug=True)
