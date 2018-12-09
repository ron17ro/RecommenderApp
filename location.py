import re
import json
from urllib.request import urlopen
from flask import jsonify
import traceback
from flask import request
import time

# try:
#     url = 'http://ipinfo.io/json'
#     response = urlopen(url)
#     data = json.load(response)
#     IP = data['ip']
#     org = data['org']
#     city = data['city']
#     country = data['country']
#     region = data['region']
#     loc = data['loc']
#     postal = data['postal']
# except:
#     url = 'http://ipinfo.io/json'
#     response = urlopen(url)
#     data = json.load(response)
#     IP = data['ip']
#     org = data['org']
#     city = data['city']
#     country = data['country']
#     region = data['region']
#     loc = data['loc']
#     postal = data['postal']

data = {}


def get_remote_addr():
    address = request.headers.get('X-Forwarded-For', request.remote_addr)
    if address is not None:
        # An 'X-Forwarded-For' header includes a comma separated list of the
        # addresses, the first address being the actual remote address.
        address = address.encode('utf-8').split(b',')[0].strip()
        ip = str(address)
        print(ip[1:])
    return ip[1:]


def getGeolocationByIp():
    try:
        ip = get_remote_addr()
        url = 'http://ipinfo.io/' + str(ip).strip("'") + '/geo'
        print(url)
        response = urlopen(url)
        time.sleep(1000)
        data = json.load(response)
        print('data' + str(data))
    except Exception:
        print('could not get the ip')
        traceback.print_exc()
        return
    return data


def my_city():
    print('Your city: {0}'.format(data['city']))
    return data['city']


def my_coordinates():
    print('Your coordinates: {0}'.format(data['loc']))
    # return loc
    return data['loc']

# def my_location():
#     print('Your IP detail\n ')
#     print('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(
#         org, region, country, city, IP))
