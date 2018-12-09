import requests
import pyowm  # importing the pyowm library
from urllib.request import urlopen
import json
import time
from keys import KEYS
#from settings import KEYS
from location import *
import traceback

# importing the key
owm = pyowm.OWM(KEYS['OpenWeatherMap'])


try:
	# setting up the endpoint for OWP
	endpoint = 'http://api.openweathermap.org/data/2.5/weather'
	payload = {'q':  my_city(), 'units': 'metric',
			'appid': KEYS['OpenWeatherMap']}
	response = requests.get(endpoint, params=payload)
	# parsing the data
	weather_data = response.json()
except:
	print('cannot connect to openweathermaps')


# compare status to weather conditions
def getWeather():
	try:
		# search for weather information based on browser's location
		observation = owm.weather_at_place(my_city())
		w = observation.get_weather()

		# get the weather status
		status = w.get_status()

	except:
		# search for weather information based on browser's location
		observation = owm.weather_at_place(my_city())
		w = observation.get_weather()

		# get the weather status
		status = w.get_status()

	# lists of weather conditions for sunny and rainy
	sunny = ['Clear', 'Clouds', 'broken clouds']
	rainy = ['Thunderstorm', 'Drizzle', 'Rain', 'Snow']

	if status in sunny:
		print('Weather looks good. Let\'s do something outdoor')
		return 'outdoor'

	elif status in rainy:
		print('It doesn\'t look so nice outside. Let\'s stay indoor today!')
		return 'indoor'

	else:
		print('please choose what type of activity you want')
		return 'io_activities'


# get the city id
def city_id():
	try:
		cityid = weather_data['id']
	except Exception:
		print('error getting the weather id ')
		traceback.print_exc()
	return cityid

# getWeather()
