from flask import Flask, render_template, request 
from location import my_location
from settings import KEYS

app = Flask("MyApp")

@app.route("/")
def display_location():
	return render_template("index.html", location = my_location(), OpenWeatherMap_API_KEY = KEYS['OpenWeatherMap'] )



if __name__ == '__main__':
    app.run(debug=True)
