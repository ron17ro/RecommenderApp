import re
import json
from urllib.request import urlopen

try:
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)
    IP = data['ip']
    org = data['org']
    city = data['city']
    country = data['country']
    region = data['region']
    loc = data['loc']
    postal = data['postal']
except:
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)
    IP = data['ip']
    org = data['org']
    city = data['city']
    country = data['country']
    region = data['region']
    loc = data['loc']
    postal = data['postal']


def getGeolocationByIp(ip):
    try:
        url = 'ipinfo.io/' + ip + '/geo'
        response = urlopen(url)
        data = json.load(response)
    except:
        print('could not get the ip')
        return
    return data['loc']


def my_location():
    print('Your IP detail\n ')
    print('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(
        org, region, country, city, IP))


def my_city():
    print('Your city: {0}'.format(city))
    return city


def my_coordinates():
    print('Your coordinates: {0}'.format(loc))
    return loc
