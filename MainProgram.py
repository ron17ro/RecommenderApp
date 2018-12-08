from flask import Flask, render_template, request
from location import *
from places import *
from keys import *
# from settings import KEYS
from weather import *
from flask import jsonify

# from emailProgram import *


app = Flask('Weather Recommendation App')

ip = ''
loc = ''


@app.route('/', methods=["POST", "GET"])
def display_location():
	try:
		ip = request.environ['REMOTE_ADDR']
		print('IP ' + ip)
	except:
		print('error getting the client ip')   
	return render_template("IOCategories.html", location=my_city(), OpenWeatherMap_API_KEY=KEYS['OpenWeatherMap'], all_places_names=all_places_names, cityId=city_id())


@app.route('/<place_type>')
def display_places_by_selected_type(place_type):
    # print(get_nearby_places(my_coordinates(), 'park', ''))
    # print('Debug - Hello')
    # print()
    # print(place_type.title())
    # nearby_places = get_nearby_places(my_coordinates(), place_type, '')

	nearby_places = get_nearby_places(my_coordinates(), place_type, '')
	return render_template("places_by_category.html", location=my_city(), OpenWeatherMap_API_KEY=KEYS['OpenWeatherMap'], all_places=nearby_places,
							all_places_names=all_places_names, Google_API_KEY=KEYS['google_API'], cityId=city_id(), place_type=place_type.title(), selected_place_category=all_places_names[place_type])


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        form_data = request.form
        name = form_data["name"]
        receiver_address = form_data["email"]
        message = form_data["message"]
        requests.post("https://api.mailgun.net/v3/sandbox92fcbfc429d24161a806e60bc92f3306.mailgun.org/messages",
                      auth=("api", KEYS['mailGun']), data={"from": "My Weather App <weatherapp@gmail.com>",
                                                           "to": KEYS['CommentEmail'],
                                                           "subject": "New Comment on Weather App",
                                                           "text": "Name: " + name + "\n" + "Email addres: " + receiver_address + "\n" + "Message: " + message})
        return render_template("IOCategories.html", location=my_city(), cityId=city_id(),
                               OpenWeatherMap_API_KEY=KEYS['OpenWeatherMap'], all_places_names=all_places_names)
    else:
        return render_template("contact.html", location=my_city(), cityId=city_id(),
                               OpenWeatherMap_API_KEY=KEYS['OpenWeatherMap'], all_places_names=all_places_names)


@app.route('/suggestions')
def display_outdoor_places():
	# print(suggestions.title() + 'you are in suggestions')
	if getWeather() == 'sunny':
		places = get_outdoor_places(my_coordinates())
	else:
		places=get_indoor_places(my_coordinates())


	return render_template("places_by_category.html", location=my_city(), OpenWeatherMap_API_KEY=KEYS['OpenWeatherMap'], all_places=places,
                           all_places_names=all_places_names, Google_API_KEY=KEYS['google_API'], cityId=city_id(), weather=getWeather())


if __name__ == '__main__':
    app.run(debug=True)
