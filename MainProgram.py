from flask import Flask, render_template, request
from location import *
from places import *
# use keys.py on heroku
from keys import KEYS
# use settings.py on local
# from settings import KEYS
from weather import *

# from emailProgram import *


app = Flask('Weather Recommendation App')


@app.route('/', methods=['POST', 'GET'])
def display_location():
        # uncommet try/except on heroku
    try:
        data = getGeolocationByIp()
    except Exception:
        print('error getting the remote ip ')
        traceback.print_exc()
        # uncommet try/except on heroku

    return render_template("IOCategories.html", location=my_city(), OpenWeatherMap_API_KEY=KEYS['OpenWeatherMap'], all_places_names=all_places_names, cityId=city_id())


@app.route('/<place_type>')
def display_places_by_selected_type(place_type):
    # print(get_nearby_places(my_coordinates(), 'park', ''))
    # print('Debug - Hello')
    # print()
    # print(place_type.title())
    # nearby_places = get_nearby_places(my_coordinates(), place_type, '')
	try:
		location=my_city()
		OpenWeatherMap_API_KEY=KEYS['OpenWeatherMap']
		nearby_places = get_nearby_places(my_coordinates(), place_type, '')
		Google_API_KEY = KEYS['google_API']
		cityId=city_id()
		# place_type = place_type.title()
	except Exception:
		print('error reading a category of places')
		traceback.print_exc()
	return render_template("places_by_category.html", location = location , OpenWeatherMap_API_KEY = OpenWeatherMap_API_KEY, all_places=nearby_places,
                           all_places_names =all_places_names, Google_API_KEY = Google_API_KEY, cityId =cityId, selected_place_category =all_places_names[place_type])


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        form_data = request.form
        name = form_data["name"]
        receiver_address = form_data["email"]
        message = form_data["message"]
        requests.post("https://api.mailgun.net/v3/sandboxa062bbcd3ac34018a2edd4420b74f6b5.mailgun.org/messages",
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
    if getWeather() =='outdoor':
        places = get_outdoor_places(my_coordinates())
    else:
        places = get_indoor_places(my_coordinates())

    return render_template("places_by_category.html", location=my_city(), OpenWeatherMap_API_KEY=KEYS['OpenWeatherMap'], all_places=places,
                           all_places_names=all_places_names, Google_API_KEY=KEYS['google_API'], cityId=city_id(), weather=getWeather())


if __name__ == '__main__':
    app.run(debug=True)
