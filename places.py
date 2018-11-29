
import requests
import json
import time
from settings import KEYS
from location import *

api_key = KEYS['google_API']


all_places_names = dict([
	('accounting', 'accounting'),
	('airport', 'airport'),
	('amusement_park', 'amusement park'),
	('aquarium', 'aquarium'),
	('art_gallery', 'art galery'),
	('atm', 'atm'),
	('bakery', 'bakery'),
	('bank', 'bank'),
	('bar', 'bar'),
	('beauty_salon', 'beauty salon'),
	('bicycle_store', 'bicycle store'),
	('book_store', 'book store'),
	('bowling_alley', 'bowling alley'),
	('bus_station', 'bus station'),
	('cafe', 'cafe'),
	('campground', 'campground'),
	('car_dealer', 'car dealer'),
	('car_rental', 'car rental'),
	('car_repair', 'car repair'),
	('car_wash', 'car wash'),
	('casino', 'casino'),
	('cemetery', 'cemetery'),
	('church', 'church'),
	('city_hall', 'city hall'),
	('clothing_store', 'clothing store'),
	('convenience_store', 'convenience store'),
	('courthouse', 'courthouse'),
	('dentist', 'dentist'),
	('department_store', 'department store'),
	('doctor', 'doctor'),
	('electrician', 'electrician'),
	('electronics_store', 'electronics store'),
	('embassy', 'embassy'),
	('fire_station', 'fire station'),
	('florist', 'florist'),
	('funeral_home', 'funeral home'),
	('furniture_store', 'furniture store'),
	('gas_station', 'gas station'),
	('gym', 'gym'),
	('hair_care', 'hair care'),
	('hardware_store', 'hardware store'),
	('hindu_temple', 'hindu temple'),
	('home_goods_store', 'home goods store'),
	('hospital', 'hospital'),
	('insurance_agency', 'insurance agency'),
	('jewelry_store', 'jewelry store'),
	('laundry', 'laundry'),
	('lawyer', 'lawyer'),
	('library', 'library'),
	('liquor_store', 'liquor store'),
	('local_government_office', 'local government office'),
	('locksmith', 'locksmith'),
	('lodging', 'lodging'),
	('meal_delivery', 'meal delivery'),
	('meal_takeaway', 'meal takeaway'),
	('mosque', 'mosque'),
	('movie_rental', 'movie rental'),
	('movie_theater', 'movie theater'),
	('moving_company', 'moving company'),
	('museum', 'museum'),
	('night_club', 'night club'),
	('painter', 'painter'),
	('park', 'park'),
	('parking', 'parking'),
	('pet_store', 'pet store'),
	('pharmacy', 'pharmacy'),
	('physiotherapist', 'physiotherapist'),
	('plumber', 'plumber'),
	('police', 'police'),
	('post_office', 'post office'),
	('real_estate_agency', 'real estate agency'),
	('restaurant', 'restaurant'),
	('roofing_contractor', 'roofing contractor'),
	('rv_park', 'rv park'),
	('school', 'school'),
	('shoe_store', 'shoe store'),
	('shopping_mall', 'shopping mall'),
	('spa', 'spa'),
	('stadium', 'stadium'),
	('storage', 'storage'),
	('store', 'store'),
	('subway_station', 'subway station'),
	('supermarket', 'supermarket'),
	('synagogue', 'synagogue'),
	('taxi_stand', 'taxi stand'),
	('train_station', 'train station'),
	('transit_station', 'transit station'),
	('travel_agency', 'travel agency'),
	('veterinary_care', 'veterinary care'),
	('zoo', 'zoo')
])

all_places = [
	'accounting',
	'airport',
	'amusement_park',
	'aquarium',
	'art_gallery',
	'atm',
	'bakery',
	'bank',
	'bar',
	'beauty_salon',
	'bicycle_store',
	'book_store',
	'bowling_alley',
	'bus_station',
	'cafe',
	'campground',
	'car_dealer',
	'car_rental',
	'car_repair',
	'car_wash',
	'casino',
	'cemetery',
	'church',
	'city_hall',
	'clothing_store',
	'convenience_store',
	'courthouse',
	'dentist',
	'department_store',
	'doctor',
	'electrician',
	'electronics_store',
	'embassy',
	'fire_station',
	'florist',
	'funeral_home',
	'furniture_store',
	'gas_station',
	'gym',
	'hair_care',
	'hardware_store',
	'hindu_temple',
	'home_goods_store',
	'hospital',
	'insurance_agency',
	'jewelry_store',
	'laundry',
	'lawyer',
	'library',
	'liquor_store',
	'local_government_office',
	'locksmith',
	'lodging',
	'meal_delivery',
	'meal_takeaway',
	'mosque',
	'movie_rental',
	'movie_theater',
	'moving_company',
	'museum',
	'night_club',
	'painter',
	'park',
	'parking',
	'pet_store',
	'pharmacy',
	'physiotherapist',
	'plumber',
	'police',
	'post_office',
	'real_estate_agency',
	'restaurant',
	'roofing_contractor',
	'rv_park',
	'school',
	'shoe_store',
	'shopping_mall',
	'spa',
	'stadium',
	'storage',
	'store',
	'subway_station',
	'supermarket',
	'synagogue',
	'taxi_stand',
	'train_station',
	'transit_station',
	'travel_agency',
	'veterinary_care',
	'zoo']




def get_nearby_places(coordinates, place_type, next_page):
	total_results = []
	URL = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
            + coordinates+'&radius=1000&key='+api_key+'&type='+place_type+'&pagetoken='+next_page)

	print(URL)

	r = requests.get(URL)
	response = r.text
	python_object = json.loads(response)
	results = python_object['results']
	for result in results:
		place_name = result['name']
		place_id = result['place_id']
		place_address_website_image=[]
		place_address_website_image.append(get_place_image_address_website(place_id))
		# print(place_name, place_address_website_image)
		if place_name is not None and place_address_website_image is not None:
			if place_address_website_image[0][0][0] is not None:
				place_address = place_address_website_image[0][0][0]
			else:
				place_address ='empty'
			if place_address_website_image[0][0][1] is not None:
				place_website = place_address_website_image[0][0][1]
			else:
				place_website = 'empty'
			if place_address_website_image[0][0][2]:
				place_image = place_address_website_image[0][0][2]
			else:
				place_image ='empty'
			total_results.append([place_name, place_address, place_website, place_image])
	# try:
	# 	next_page_token = python_object['next_page_token']
	# except KeyError:
	# 	# no next page
	# 	print('Key Error')
	# 	return
	# time.sleep(1)
	# get_nearby_places(coordinates, place_type, next_page_token)
	# print('What is this'+str(total_results))
	return total_results


def get_place_image_address_website(place_id):
	reqURL = ('https://maps.googleapis.com/maps/api/place/details/json?placeid='
           + place_id+'&key='+api_key)
	r = requests.get(reqURL)
	response = r.text
	python_object = json.loads(response)
	# place_image = []
	place_attr = []
	try:
		place_details = python_object["result"]

		#get website
		if 'website' in place_details  and place_details['website'] is not None:
			place_website = place_details['website']
		else:
			place_website = 'empty'

		# get photo ref
		if 'photos' in place_details:
			place_image = place_details['photos'][0]['photo_reference']
		else:
			place_image = 'empty'

		# get place address
		if 'formatted_address' in place_details and place_details['formatted_address'] is not None:
			place_address = place_details['formatted_address']
		elif 'adr_address' in place_details and  place_details['adr_address'] is not None:
			place_address = place_details['adr_address']
		else:
			place_address = 'empty'
		place_attr.append([place_address, place_website, place_image])
		return place_attr
	except:
		# place_attr.append(['empty', 'empty', 'static/images/indoor.jpg'])
		print("err getting place details")


# get_nearby_places(my_coordinates(), 'park', '')

# print(total_results)
