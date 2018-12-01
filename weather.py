import requests
import pyowm #importing the pyowm library
from urllib.request import urlopen
import json
import time
from settings import KEYS
from location import *


#importing the key
owm = pyowm.OWM(KEYS['OpenWeatherMap'])

try:
    #search for weather information based on browser's location
    observation = owm.weather_at_place(my_city())
    w = observation.get_weather()

    #get the weather status
    status = w.get_status()
except:
    observation = owm.weather_at_place(my_city())
    w = observation.get_weather()
    status = w.get_status()

# lists of weather conditions for sunny and rainy
sunny = ["Clear", "Clouds"]
rainy=["Thunderstorm", "Drizzle","Rain","Snow"]


#setting up the endpoint for OWP
endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q":  my_city(), "units":"metric", "appid":"387c8ff8556cd0350850870394fcb533"}
response = requests.get(endpoint, params=payload)

#parsing the data
data = response.json()


#compare status to weather conditions
def getWeather():
    if status in sunny:
        print ("Weather looks good. Let's do something outdoor")
    elif status in rainy:
        print ("It doesn't look so nice outside. Let's stay indoor today!")

#get the city id
def city_id():
    return data["id"]