import requests
import pyowm
from urllib.request import urlopen
import json
import time
from settings import KEYS
from location import *


#importing the key
owm = pyowm.OWM(KEYS['OpenWeatherMap'])

#search for weather information based on browser's location
observation = owm.weather_at_place(my_city())
w = observation.get_weather()

#get the weather status
status = w.get_status()

# lists of weather conditions for sunny and rainy
sunny = ["Clear", "Clouds"]
rainy=["Thunderstorm", "Drizzle","Rain","Snow"]


#compare status to weather conditions
def getWeather():
    if status in sunny:
        print ("Weather looks good. Let's do something outdoor")
    elif status in rainy:
        print ("It doesn't look so nice outside. Let's stay indoor today!")

