from flask import Flask, render_template, request 
from location import *
from places import *
from settings import KEYS
from weather import *


app = Flask('MyApp')

@app.route('/')
def display_location():
    
    return render_template("IOCategories.html", location = my_city(), cityId=city_id(),OpenWeatherMap_API_KEY = KEYS['OpenWeatherMap'], all_places_names = all_places_names)

@app.route('/<place_type>')
def disply_places_by_selected_type(place_type):
	# print(get_nearby_places(my_coordinates(), 'park', ''))
	# print('Debug - Hello')
	# print()
	nearby_places = get_nearby_places(my_coordinates(), place_type, '')
	return render_template("places_by_category.html", location = my_city(),cityId=city_id(), OpenWeatherMap_API_KEY = KEYS['OpenWeatherMap'], all_places = nearby_places,
		all_places_names = all_places_names, Google_API_KEY=KEYS['google_API'])


@app.route("/contact", methods=['POST','GET'])
def contact():
    if request.method == 'POST':
        return render_template("IOCategories.html", location = my_city(), cityId=city_id(),OpenWeatherMap_API_KEY = KEYS['OpenWeatherMap'], all_places_names = all_places_names)
    else:
        return render_template("contact.html", location = my_city(), cityId=city_id(),OpenWeatherMap_API_KEY = KEYS['OpenWeatherMap'], all_places_names = all_places_names)

if __name__ == '__main__':
    app.run(debug=True)
