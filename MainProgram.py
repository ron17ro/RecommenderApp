from flask import Flask, render_template, request 
from location import *
from places import *
from settings import KEYS


app = Flask('MyApp')

@app.route('/')
def display_location():
    
    return render_template("IOCategories.html", location = my_city(), OpenWeatherMap_API_KEY = KEYS['OpenWeatherMap'], all_places_names = all_places_names)

@app.route('/<place_type>')
def disply_places_by_selected_type(place_type):
	# print(get_nearby_places(my_coordinates(), 'park', ''))
	# print('Debug - Hello')
	# print()
	print('Hi')
	nearby_places = get_nearby_places(my_coordinates(), 'park', '')
	return render_template("places_by_category.html", location = my_city(), all_places = nearby_places,
		all_places_names = all_places_names, Google_API_KEY=KEYS['google_API'])


if __name__ == '__main__':
    app.run(debug=True)
