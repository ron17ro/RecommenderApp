
import requests
import json
import time

# use keys.py on heroku
from keys import KEYS
# use settings.py on local
# from settings import KEYS

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

outdoor_categories = dict([
	('amusement_park', 'amusement park'),
	('campground', 'campground'),
	('park', 'park'),
	('stadium', 'stadium'),
	('travel_agency', 'travel agency'),
	('zoo', 'zoo')
])

indoor_categories = dict([
	# ('bar', 'bar'),
	('art_gallery', 'art galery'),
	('cafe', 'cafe'),
	# ('gym', 'gym'),
	('museum', 'museum'),
	('restaurant', 'restaurant'),
	# ('spa', 'spa'),
	# ('supermarket', 'supermarket')
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


	# total_results = [['Dublin', 'Dublin, Ireland', 'empty', 'CmRaAAAAcKrsicNiEPbgHeMHM9PxuRRG43D-SYKROdtw4d66QXvIweRzkFpgta-pobJ2AKVwD5tmZrniFZjIWQZpziii9oHOWx4CloJsmB6DvlNUkREp_cP9H8-aMRRrHxcpnbANEhAUMSoGa7QlkslejF6yRFk3GhQFHHhNt_377zqnuWeK7ChPef69LA', 'empty', 'empty', 'favicon.ico'], ['Mespil Hotel', '50-60 Mespil Rd, Dublin 4, D04 E7N2, Ireland', 'http://www.mespilhotel.com/', 'CmRaAAAAmJvzlzG7dW2oR_OcprvZ42SYwPXoUrYPqY_Dc4HIMOleZXEVp6zyXrss3Ecx2mPIcmpeZhmajVK2wy-BKMWxV7j8I8ByUh9EmS5xFFdMmOTuKqNQAaZQgUsHw4DBIkLtEhDNr4oX2MYGpNaG1J4dMBYwGhRvECH8NPJs4SoMOts-BrqHB3x5mw', True, ['Monday: Open 24 hours', 'Tuesday: Open 24 hours', 'Wednesday: Open 24 hours', 'Thursday: Open 24 hours', 'Friday: Open 24 hours', 'Saturday: Open 24 hours', 'Sunday: Open 24 hours'], 'favicon.ico'], ['Dylan Hotel Dublin', 'Eastmoreland Pl, Dublin, Ireland', 'http://www.dylan.ie/', 'CmRaAAAAhZRUhlv4VSks2_nLcel7Sc61N5_fqcDJRHVyB_o4zR17r1UAPCL8ZYz4efsWqAhgnNXO0q9ozbsI25Tf92rCVYBDHGvV8PkJJc9O_2RewRp0PhNde6dw51HL1hH2uL8qEhAA_BLjTjuaBedhzXbEHY1aGhTDHRrBrG7MkWcSYtbZwXWqaZ1G_w', True, ['Monday: Open 24 hours', 'Tuesday: Open 24 hours', 'Wednesday: Open 24 hours', 'Thursday: Open 24 hours', 'Friday: Open 24 hours', 'Saturday: Open 24 hours', 'Sunday: Open 24 hours'], 'favicon.ico'], ['Lansdowne Hotel', '27 -29 Pembroke Rd, Dublin 4, Ireland', 'http://www.lansdownehotel.ie/', 'CmRaAAAA1SECfESgQJNiA9R5N-PDdpFO0ZowC7sspVTxAnwjyNtiWzl8WfdMrHctSG8aIDkOPjDca7n5ji_SFExOYrn9g7ChN7spDa5jRizA0UnZClTUFTcllv42FUEp6mpVE8p1EhASUD5dG-N9bQC-Vf9OsBorGhSvOkY8NCfJEJy1C35Ske4LeAR70Q', 'empty', 'empty', 'favicon.ico'], ['Conrad Dublin', "Earlsfort Terracе, Saint Kevin's, Dublin 2, D02 V562, Ireland", 'http://conradhotels3.hilton.com/en/hotels/dublin/conrad-dublin-DUBHCCI/index.html?WT.mc_id=zELWAKN0EMEA1HI2DMH3LocalSearch4DGGenericx6DUBHCCI', 'CmRaAAAATdedZBHyFvjFNhfix0BEtbde32XYMGqJMHtbHVPrMGivDuqGxKdoFS8dcgcEOJWNkX2xG0azjOvXLbs_5DDTIHEj19Bzh2ZBa4kUr69r4jDwQA_Cqf0UJ9wU_jl3zPyzEhC9ae5usLk-ghC-2DpEQCDDGhRraOMXQQScFr_hMJcRCoOdWiIFFQ', 'empty', 'empty', 'favicon.ico'], ['The Merrion Hotel Dublin', 'Merrion Street Upper, Dublin 2, Ireland', 'http://www.merrionhotel.com/', 'CmRaAAAAKilrgKDQQ9kgusy21Qcuy_M1iqo-cNkCyp3n9WeNNwvrnPqkNs9jlFL0FKUOO8QaeW7s14c8WNNqVh1QjJGjsfNmHi5xbUMat3vJ1seLvYBaH2Wyg5SEvVdIC8JLOtCKEhDai7pzOX-loLK2TjdCS9xIGhT26VjtzWzkeCwa8rcMUkeHLZXacA', True, ['Monday: Open 24 hours', 'Tuesday: Open 24 hours', 'Wednesday: Open 24 hours', 'Thursday: Open 24 hours', 'Friday: Open 24 hours', 'Saturday: 12:00 AM – 11:59 PM', 'Sunday: Open 24 hours'], 'favicon.ico'], ['Waterloo House', '10 Waterloo Rd, Dublin 4, Co. Dublin, D04 T651, Ireland', 'http://waterloohouse.ie/', 'CmRaAAAA0wyfqmPMEZENkdRwpFb9Rz7m9CxA4GHSMcL2vS5trXN90sAEe_ErthZdpfWZcGDSAqIqmmSErsyFmjoIKOEZ-ZvTGVUTyX5V2Ojr0QE2je1Wd5N1Et9t5IhBLFU9C7vBEhCC7SL1CRxBeEn-9ew6ue6PGhR4J1i9_irVkaGzkS8WvHZlpldjKw', 'empty', 'empty', 'favicon.ico'], ['Leeson Inn Downtown', "24 Lower Leeson Street, Saint Kevin's, Dublin, Ireland", 'http://www.leesoninndowntown.com/', 'CmRaAAAA4WSn-KZ2ypbB6b7kv0GmV0srhnziOqth1Y_WN-hEJKazr67SH34nNPzIa_T7M1A5d1oVcCxn7t5aI0x7CK5TtD6RWAdyCgv2SUqAzulX9RLqIseqNh7oxKzaTlavjwqcEhDoaVd6ZBCSlfDwo1lA4tlQGhSmRZ3stL_iwgor0jLsLeK7yWXTzQ', 'empty', 'empty', 'favicon.ico'], ['Clayton Hotel Burlington Road', 'Leeson Street Upper, Dublin, D04 A318, Ireland', 'https://www.claytonhotelburlingtonroad.com/', 'CmRaAAAAoT8XD2m6oneHwzKpbCPQnlSR-fiX5iI7PKzGgYl-7sfDk-tZkLxvHKIGoWO7v6eVCVZW563u6dAR5sOZfpsQIsBzCeO04YzqCFlX00OQ0M8PL60UHuSG5ksiIKC7uGy_EhD4aTJcnOhkZ--VtZ0Bz1VsGhRKJuNkRb9p0iGrvqAB7JiQ8UijCg', 'empty', 'empty', 'favicon.ico'], ['Leeson Apartments', '1 Leeson Street Upper, Dublin 4, D04 AH22, Ireland', 'https://www.leesonapartments.com/', 'empty', 'empty', 'empty', 'favicon.ico'], ['Harvest Moon Centre', '24 Baggot Street Lower, Dublin 2, D02 EW26, Ireland', 'http://www.harvestmoon.ie/', 'CmRZAAAALt4cshhi4PDUWxfr4jAgBZ0NoP9tuzlM1S1nlWidVI6x8NYW3Z1reKPYgyRY4LAIQJHxpk2NPFbj_DGPHUP9iL2j2aBEB0-PGZjJnANojiPsfOffI6zyqmMht3GSn4V8EhCHRIEnqB4dEPw4iZ4lMmwjGhQHgx0jhUe1qBnX8ZlRuOjnSFtWdw', False, ['Monday: 10:00 AM – 9:00 PM', 'Tuesday: 10:00 AM – 9:00 PM', 'Wednesday: 10:00 AM – 9:00 PM', 'Thursday: 10:00 AM – 9:00 PM', 'Friday: 10:00 AM – 9:00 PM', 'Saturday: 11:00 AM – 8:00 PM', 'Sunday: 11:00 AM – 7:00 PM'], 'favicon.ico'], ['Matt The Thresher', '31-32 Pembroke Street Lower, Dublin 2, Ireland', 'http://mattthethresher.ie/', 'CmRaAAAAXdr7nyUKgS8Wf5eQNer4dDPkuKFQqJfZ5UOk2nkLGURIBBAkt4luFQEzgZPnwCSg5dX-xwWXcRnWpsyvf_lkgbTZXXHSveWKmT9K5qLVrkBTqLSynDVxkwqhv42sNfLnEhBwU0KNPnZl3tq174cSols9GhTk812VBWUg_MrHJdr8nBVaKTXm1w', False, ['Monday: 10:00 AM – 9:45 PM', 'Tuesday: 10:00 AM – 9:45 PM', 'Wednesday: 10:00 AM – 9:45 PM', 'Thursday: 10:00 AM – 9:45 PM', 'Friday: 10:00 AM – 9:45 PM', 'Saturday: 12:00 – 9:45 PM', 'Sunday: 12:30 – 8:30 PM'], 'favicon.ico'], ['Toners', '139 Baggot Street Lower, Dublin 2, Ireland', 'http://www.tonerspub.ie/', 'CmRaAAAAuhfYaHVNs42NxM-Or5oPiz2gFTRBX4Kfn1S3G5DH9UrD_A6nYAbEhK8sDTuF42H9Qzhl7cF-viV4NRhcQN1BHYmWiEMHeyvVsNearHMAy-WNsZvpSvmQiC_0LlUXkZabEhBDEw_PLpDqVOQMj2z6GH7fGhSvRcmJs1Xt2wjhJnozzQihkOMRKw', True, ['Monday: 10:30 AM – 11:30 PM', 'Tuesday: 10:30 AM – 11:30 PM', 'Wednesday: 10:30 AM – 11:30 PM', 'Thursday: 10:30 AM – 11:30 PM', 'Friday: 10:30 AM – 12:30 AM', 'Saturday: 10:30 AM – 12:30 AM', 'Sunday: 11:30 AM – 11:30 PM'], 'favicon.ico'], ['Blow Salons', '144 Leeson Street Upper, Dublin, D04 Y564, Ireland', 'http://www.blow.ie/?utm_source=GMBlisting&utm_medium=Organic', 'CmRaAAAAkPng_nNeBUH3kR77AxXlLXU2d-h-C2a7R5MX5pvfsiX8hfwS7iw1vE_LQIOSB0Q6ANocpqWokmCB1g6Lttye0DGa4e2uADcpYArOOOHZSHVwjPtzj5Yo3Ie8ZvXikZPDEhBlqTcgDoEE0-JjNRcOjwtPGhQkC0075CIX6r94uyXNFfDIbnKdDA', False, ['Monday: 6:45 AM – 7:30 PM', 'Tuesday: 6:45 AM – 7:30 PM', 'Wednesday: 6:45 AM – 7:30 PM', 'Thursday: 6:45 AM – 7:30 PM', 'Friday: 6:45 AM – 7:30 PM', 'Saturday: 9:00 AM – 6:00 PM', 'Sunday: 10:00 AM – 4:00 PM'], 'favicon.ico'], ['Active Physiotherapy and Acupuncture Clinic', '112c Lower Baggot Street, Dublin 2, Grand Canal Dock, Dublin, Co. Dublin, Ireland', 'empty', 'empty', False, ['Monday: 8:30 AM – 6:00 PM', 'Tuesday: 8:30 AM – 7:00 PM', 'Wednesday: 8:30 AM – 6:00 PM', 'Thursday: 8:30 AM – 7:30 PM', 'Friday: 8:30 AM – 6:00 PM', 'Saturday: Closed', 'Sunday: Closed'], 'favicon.ico'], ['Cpl Resources Plc', '8-, 34 Percy Pl, Dublin 4, Ireland', 'http://www.cpl.ie/', 'CmRaAAAAhfhjksFZk9a9g-rZEqlDkGt9J9uSERAkqTYugjujw0Q5TnM0uPRPxXqAHSEze1C7tenYieRTft1i66joLIf7lWWqgZwLiyOakButQcjTk1lGRVr5tBmo59GnVFXrgZxZEhACIhOjMx_OIZfVxqf7P12eGhR-WXOiD5stVbMxpctbaSaEcXHM5g', False, ['Monday: 9:00 AM – 5:30 PM', 'Tuesday: 9:00 AM – 5:30 PM', 'Wednesday: 9:00 AM – 5:30 PM', 'Thursday: 9:00 AM – 5:30 PM', 'Friday: 9:00 AM – 5:30 PM', 'Saturday: Closed', 'Sunday: Closed'], 'favicon.ico'], ['Chez Max - Baggot St', '133 Lower Baggot St, Dublin 2, Co. Dublin, Ireland', 'http://www.chezmax.ie/baggot/', 'CmRaAAAAnDqNhLoUi2jHftke82XsEq9orv_4v5XUIp1fKsKxfiIXeG8PIJCpmqcl86d8y0A-bHkTVC4qTbL1pd-qwNzLaxxyXWLpLmUwHa7RswgDTA5exRjJb4NUDdcOilZM9LRLEhCEB2EbaOVCqUkn0XPm581tGhSeEG4nBPTpQuys4TXfHicjdPaTXQ', True, ['Monday: 12:00 – 3:30 PM, 5:30 – 10:00 PM', 'Tuesday: 12:00 – 3:30 PM, 5:30 – 10:00 PM', 'Wednesday: 12:00 – 3:30 PM, 5:30 – 10:00 PM', 'Thursday: 12:00 – 3:30 PM, 5:30 – 10:00 PM', 'Friday: 12:00 – 3:30 PM, 5:30 – 11:00 PM', 'Saturday: 11:00 AM – 4:00 PM, 5:30 – 11:00 PM', 'Sunday: Closed'], 'favicon.ico'], ['KD Media', '5 Fitzwilliam Pl, Grand Canal Dock, Dublin, Ireland', 'http://www.kinkydevil.ie/', 'empty', 'empty', 'empty', 'favicon.ico'], ['Abbeyleigh House', 
	# '28 Leeson Street Upper, Dublin 4, D04 XF72, Ireland', 'https://abbeyleighhouse.wordpress.com/', 'CmRaAAAAD1iVd7KdHbk39ugLWcXllz83HRmgZfzPbRUiIQOqWvYpBPV0RPcNxNoCHqiJu0yMqDdIJgfTIC5iqPguwVo76USf6BtrrHQawMY4PD82hPnSHQkKfOkN6UtHAW1Hz797EhA-hdtW7lidmdkyY4fajr-pGhRPgoUR6C4SuqNcCfvZVlujOmbmww', 'empty', 'empty', 'favicon.ico'], ['Rathmines', 'Rathmines, Co. Dublin, Ireland', 'empty', 'CmRaAAAAW3tBnBnQCttaOfcjL-5yegiAzQEIjbcs-UDG74ZaZALxQtuWeHtSkLgxptNr7WPcNNNty5LP5zK1qhllmpcZNWAUGgvB8vj4FX4BH9nYsDQOixW4adP-TwihykNbUGM_EhB1A4yy4xqV2r8Yq9WeLXCKGhStNzNm1ztjqGuw6R6xKmirsPY2Xw', 'empty', 'empty', 'favicon.ico'],['Dublin', 'Dublin, Ireland', 'empty', 'CmRaAAAAyNy_BNv73SLfUGgHUUUR0hC4sj7TsIbhA0TBd61sziivm4Ve0YaVBZVigb4_TYhVAXKJQTCyF2I3IjErjlbv34KFnt-6c27RJsquZ1_MqfX7rjmxbt8c7fuyq1GcVQEDEhCRF_7Kcj_SpY8RDo2m0OORGhTJ-WYQqmaNZq1TNajAe3pY0XfEXA', 'empty', 'empty', 'suggestions'], ['Mespil Hotel', '50-60 Mespil Rd, Dublin 4, D04 E7N2, Ireland', 'http://www.mespilhotel.com/', 'CmRaAAAAWouwiYP3gU0pUgv3OPNItje5jrdviZQeLqo5ZdoMP2yYqdQ74pEwB7pDi3IW2MzypIQ5X8GkCWpW_BPHC-ciigLtB8XNxAMWqUzbEKnIMaVMNoFeEKGio-bjou99eWkvEhBRL-zB8ZKYeL4xpKFQTWuwGhSdVeESjQ1NDNYpO-SuOBAsiEbQUg', True, ['Monday: Open 24 hours', 'Tuesday: Open 24 hours', 'Wednesday: Open 24 hours', 'Thursday: Open 24 hours', 'Friday: Open 24 hours', 'Saturday: Open 24 hours', 'Sunday: Open 24 hours'], 'suggestions'], ['Dylan Hotel Dublin', 'Eastmoreland Pl, Dublin, Ireland', 'http://www.dylan.ie/', 'CmRaAAAAVz-MYxU-J-QdgVxgVH3fyvnsRA5T2eni5_LIRcysW6mVApulrGKywGGnlGuzSdLoainzxEQidFxHLY_IUMav7zPS3abtUtjHTGay97AsKSHpgzY9YCfsGNa1cVohJgltEhCXXnU73dz4aXcE7DPy8Gg0GhTnJROx8s44l-S7KX2F2Y15pLsC-w', True, ['Monday: Open 24 hours', 'Tuesday: Open 24 hours', 'Wednesday: Open 24 hours', 'Thursday: Open 24 hours', 'Friday: Open 24 hours', 'Saturday: Open 24 hours', 'Sunday: Open 24 hours'], 'suggestions'], ['Lansdowne Hotel', '27 -29 Pembroke Rd, Dublin 4, Ireland', 'http://www.lansdownehotel.ie/', 'CmRaAAAAtbINYBms6bcaSbpShjXRCkzCqFqFTkctPhoymRjysDLCQdzEPQRymqKMD6kP3q7T2q-m82-MM1xGA13XMfho6scE5wElzao7dKpdoe37sNY63NQPgFxPo2Ldft1RhCwoEhDw4igZFf1HWEdIXZ1Nb6ZLGhQPG09AXk5YySlgS7JteYM_6gw1Nw', 'empty', 'empty', 'suggestions'], ['Conrad Dublin', "Earlsfort Terracе, Saint Kevin's, Dublin 2, D02 V562, Ireland", 'http://conradhotels3.hilton.com/en/hotels/dublin/conrad-dublin-DUBHCCI/index.html?WT.mc_id=zELWAKN0EMEA1HI2DMH3LocalSearch4DGGenericx6DUBHCCI', 'CmRaAAAAW3htjG9b5BTIuv5LAgU1mgT3Vt9KkPT8GzGP3vUyy_U6e0tZ9Jo7Qzshh0gRKYSml9m76-36FDJY1eZbdwMUSdAt3Zoa8YdL1zOzrst2s4hW2qnX1t8jc8UaFOo4ue_eEhBAxwUYZ52vAUiijuaX8EcJGhRQKfIC3DZTSagOhDGDdBxTbK-PkA', 'empty', 'empty', 'suggestions'], ['The Merrion Hotel Dublin', 'Merrion Street Upper, Dublin 2, Ireland', 'http://www.merrionhotel.com/', 'CmRaAAAAXwgUFK-BgRMGX0AdPx7DP7EwnJcJRjdZPZGOev1AVsMVv1rt6tSA_5S_Dj1RxBD2ozOOAs5vyt3aDBNUHNzoa57v_XZzwtaT4tjRGKrWW5aGGNJU2D73wqFx5FUq3vVZEhBZxh_clwfCqeGyNCWfEPLUGhR-Z9b6wjwLp2VeKXGjVPgIJjPk1Q', True, ['Monday: Open 24 hours', 'Tuesday: Open 24 hours', 'Wednesday: Open 24 hours', 'Thursday: Open 24 hours', 'Friday: Open 24 hours', 'Saturday: 12:00 AM – 11:59 PM', 'Sunday: Open 24 hours'], 'suggestions'], ['Waterloo House', '10 Waterloo Rd, Dublin 4, Co. Dublin, D04 T651, Ireland', 'http://waterloohouse.ie/', 'CmRaAAAAvDnbpwmuCXXRKa5gF0peyt-cMTsIOYd0qAzJC8jpmn1QonoUYamoGyk82d-2EMiwKoDvWJ8NU0WdvQ_pIsC1cRQxWsaPHav1oVdCOJ6_m6q2AgP7Q9YWoxsrXQjM4B68EhCC9ByGOU5AKzroB82jLVjPGhRmByN4DNJJH9j3MWPOQ7XPzjkmKw', 'empty', 'empty', 'suggestions'], ['Leeson Inn Downtown', "24 Lower Leeson Street, Saint Kevin's, Dublin, Ireland", 'http://www.leesoninndowntown.com/', 'CmRaAAAApWOw4O4GuslU3O5V6s57RFhRdqD8toEBKwI6T4eVLxs2NvzBofedxreS1srXCEFCNMNRLLS9Va7gaTa5JXNCerIq3re06VW1B4SmNPaV7IJsbNUijtVgzY9lyBN2JWX8EhDrcnObvFaflyczjsWY0_3zGhRHpvtSV8XvzVsbrC2PqEgmhbA2yA', 'empty', 'empty', 'suggestions'], ['Clayton Hotel Burlington Road', 'Leeson Street Upper, Dublin, D04 A318, Ireland', 'https://www.claytonhotelburlingtonroad.com/', 'CmRaAAAAzwcI7SfDkngxGq7MHFyBZhY9RvI_jgqWOhgxscp24jkTsplFKBe3bizNk7gm3PnJNeVMFSpKxOkDux7QeFdKIIwjmEhiZDx41m2hdX3FQj_T6Xk3V9BwgUbP519VgUQ1EhCxIO8N09vd2l-Qo5ye7VxfGhRtigho-T1Ed8iSJyPx0WzpijaUVQ', 'empty', 'empty', 'suggestions'], ['Leeson Apartments', '1 Leeson Street Upper, Dublin 4, D04 AH22, Ireland', 'https://www.leesonapartments.com/', 'empty', 'empty', 'empty', 'suggestions'], ['Harvest Moon Centre', '24 Baggot Street Lower, Dublin 2, D02 EW26, Ireland', 'http://www.harvestmoon.ie/', 'CmRZAAAAYObqAs6Y2D0M5HK38fDViT8UIOwK6oeB8ekkS_CkKRs7KIe6k7k2zCSFlt0qLeYmr7v8zHGfFjhMyyyhDbihJWqnhWSjovvr96BiLj4yw_GpcUs39x6mwRFHyONNGWzNEhDCssm2lTeCUfz5CA6eZbsxGhT_OLufsDt7nr4mQC5pEsX8z9UwJw', False, ['Monday: 10:00 AM – 9:00 PM', 'Tuesday: 10:00 AM – 9:00 PM', 'Wednesday: 10:00 AM – 9:00 PM', 'Thursday: 10:00 AM – 9:00 PM', 'Friday: 10:00 AM – 9:00 PM', 'Saturday: 11:00 AM – 8:00 PM', 'Sunday: 11:00 AM – 7:00 PM'], 'suggestions'], ['Matt The Thresher', '31-32 Pembroke Street Lower, Dublin 2, Ireland', 'http://mattthethresher.ie/', 'CmRaAAAAZICf3QBqGC_5zwn1gkEGhbRlopp0Dnq88L2sPIub8qkI3gID6aMTGMEkjbhlnP8y_pyCENvCpJtDSOSkeNzOzEAQ0KEJ2PEVlficKzYAl3ePOSaC3CDXCkcuig21vYZXEhCeapBmrk5hRTtBOm14Aie6GhTtJYm7_N2cjYBjiFP8_wmikasRRw', False, ['Monday: 10:00 AM – 9:45 PM', 'Tuesday: 10:00 AM – 9:45 PM', 'Wednesday: 10:00 AM – 9:45 PM', 'Thursday: 10:00 AM – 9:45 PM', 'Friday: 10:00 AM – 9:45 PM', 'Saturday: 12:00 – 9:45 PM', 'Sunday: 12:30 – 8:30 PM'], 'suggestions'], ['Toners', '139 Baggot Street Lower, Dublin 2, Ireland', 'http://www.tonerspub.ie/', 'CmRaAAAA67Zy3olP81t7wmwR4TQJ9ffs-nwZQVkxdg79Pg-arHq9Gcxl9E-sdJMwanRkp7ySo3SFukjcNBJpBy35t5WctFRDsLuPuEld9zQ7xmty-Duy6GxEIqG9wvC7sa03GaoeEhDX9LgSSxiRsw4O-LWEiLxMGhSl9GVfagSNpFbS_QtvK27IXIlBKQ', True, ['Monday: 10:30 AM – 11:30 PM', 'Tuesday: 10:30 AM – 11:30 PM', 'Wednesday: 10:30 AM – 11:30 PM', 'Thursday: 10:30 AM – 11:30 PM', 'Friday: 10:30 AM – 12:30 AM', 'Saturday: 10:30 AM – 12:30 AM', 'Sunday: 11:30 AM – 11:30 PM'], 'suggestions'], ['Blow Salons', '144 Leeson Street Upper, Dublin, D04 Y564, Ireland', 'http://www.blow.ie/?utm_source=GMBlisting&utm_medium=Organic', 'CmRaAAAA_XPy_RvVR7zDv2hRTCbOa1xLWbtTh9UrdL0BpbXU5FGjUMFn_2lMuZ_debgbLcKjmLRAlgeOoQNfyTY6wATHXRxdtyx6U1g2ukMRUIy1ycAurxtwUQbhGooW4Fvm9QbuEhC-h5Y_6UdM8witpGNWPjtzGhRGtJFltWUc7Pr3JcYZXqoXr5iNLg', False, ['Monday: 6:45 AM – 7:30 PM', 'Tuesday: 6:45 AM – 7:30 PM', 'Wednesday: 6:45 AM – 7:30 PM', 'Thursday: 6:45 AM – 7:30 PM', 'Friday: 6:45 AM – 7:30 PM', 'Saturday: 9:00 AM – 6:00 PM', 'Sunday: 10:00 AM – 4:00 PM'], 'suggestions'], ['Active Physiotherapy and Acupuncture Clinic', '112c Lower Baggot Street, Dublin 2, Grand Canal Dock, Dublin, Co. Dublin, Ireland', 'empty', 'empty', False, ['Monday: 8:30 AM – 6:00 PM', 'Tuesday: 8:30 AM – 7:00 PM', 'Wednesday: 8:30 AM – 6:00 PM', 'Thursday: 8:30 AM – 7:30 PM', 'Friday: 8:30 AM – 6:00 PM', 'Saturday: Closed', 'Sunday: Closed'], 'suggestions'], ['Cpl Resources Plc', '8-, 34 Percy Pl, Dublin 4, Ireland', 'http://www.cpl.ie/', 'CmRaAAAAFUSOCXTclgMILDTnJhlNIQ4RzW5-G_v9cJvD6OMUCPvKyd6S8mPPZr-YIIM8ZlM5OpS9E94DqdPmGJocqQ3xmd-UvbZ0lVNXyjTGKLWoOGQgtiCruw9tQuHy36fS14WmEhBpOteZ8wG9BOE9upuJr-K0GhT7A-HZay4Fx7tNaLkqSu527i4aTA', False, ['Monday: 9:00 AM – 5:30 PM', 'Tuesday: 9:00 AM – 5:30 PM', 'Wednesday: 9:00 AM – 5:30 PM', 'Thursday: 9:00 AM – 5:30 PM', 'Friday: 9:00 AM – 5:30 PM', 'Saturday: Closed', 'Sunday: Closed'], 'suggestions'], ['Chez Max - Baggot St', '133 Lower Baggot St, Dublin 2, Co. Dublin, Ireland', 'http://www.chezmax.ie/baggot/', 'CmRaAAAAesUOPo3rgt5_eCqxbCVwOGextuwrK6obmX2X29FUjsWiEI2qtZRrOdFBu1e1OqYEXqovOQF-W9wpIEiY-KaC99t9rO0WioJeVWK7zCQ-7qq3FD8WRxuyfFwR8Ai9NJD0EhD3NG_pcrp6GfQWHGarce9HGhTn971jgWEdXNZH1U0iomCg7KVHDA', True, ['Monday: 12:00 – 3:30 PM, 5:30 – 10:00 PM', 'Tuesday: 12:00 – 3:30 PM, 5:30 – 10:00 PM', 'Wednesday: 12:00 – 3:30 PM, 5:30 – 10:00 PM', 'Thursday: 12:00 – 3:30 PM, 5:30 – 10:00 PM', 'Friday: 12:00 – 3:30 PM, 5:30 – 11:00 PM', 'Saturday: 11:00 AM – 4:00 PM, 5:30 – 11:00 PM', 'Sunday: Closed'], 'suggestions'], ['KD Media', '5 Fitzwilliam Pl, Grand Canal Dock, Dublin, Ireland', 'http://www.kinkydevil.ie/', 'empty', 'empty', 'empty', 'suggestions'], ['Abbeyleigh House', 
	# '28 Leeson Street Upper, Dublin 4, D04 XF72, Ireland', 'https://abbeyleighhouse.wordpress.com/', 'CmRaAAAAUhFAJjte9geF5gFu3OfTAkAV0xTxuoT6W8tJORUHt5rUxNE9G5UEkdGqX4-ZCd_iaNxXOKu0SE1eCQ6M7Bb5dG-afq5vhsfkXvUDrZ1mmCrv1HfJHbehEIPFRw173XtEEhCb4QyNb4wlRNKimPydpO2dGhTv8NyXfhyCClJobthwEcmfvefu9w', 'empty', 'empty', 'suggestions'], ['Rathmines', 'Rathmines, Co. Dublin, Ireland', 'empty', 'CmRaAAAAvPrNW-Nv4AwkMtl2XT_v6lf-Kmd3Mu4W0kVgCc_wtNwBItBzoNfx4tyzw33oKsrawJ4ICUk730F56kz6DUcXPzPJRci5uP-5M0m--dQNdfCgGywUWsKhtk5zhHuf7oMqEhDR_VbG7nH_OxQzLuO0EvB5GhQhBwoI6zLimbTZxfx5yHLi0GSx8g', 'empty', 'empty', 'suggestions'],['Dublin', 'Dublin, Ireland', 'empty', 'CmRaAAAAC94u9SZSaT2m4PA4YdNEKqMxBBOPAAq_WbPeNeL7bOtWDIAKryujA_qs24Jsc86qdVoAumiysfYqtMCKASHwc3WZwpB3WEydC5iSnWxhnLXOU4eeiXc5ILug9zC1z-W4EhCkIkeuyNG42NG4AN7tvs_tGhRMw569iwdoq_pkaXhDtaNThS_ZTA', 'empty', 'empty', 'favicon.ico'], ['Mespil Hotel', '50-60 Mespil Rd, Dublin 4, D04 E7N2, Ireland', 'http://www.mespilhotel.com/', 'CmRaAAAAlWfysAl4VzViyuYKYLd05ch5WC4oPxzpyLmK89FZbqMQBEZEFYt5qwyww7RT5UPan8gA9vBa9tv0wfEl1O4rDqyftQpC5DQeodCMBoQ0PiaKoumb2h248o0BvHDknMi0EhDugxa1374IVRkEzRt4M0pLGhTJ8iYjwtZEIJ5MaUnYd8QQ1_rzng', True, ['Monday: Open 24 hours', 'Tuesday: Open 24 hours', 'Wednesday: Open 24 hours', 'Thursday: Open 24 hours', 'Friday: Open 24 hours', 'Saturday: Open 24 hours', 'Sunday: Open 24 hours'], 'favicon.ico'], ['Dylan Hotel Dublin', 'Eastmoreland Pl, Dublin, Ireland', 'http://www.dylan.ie/', 'CmRaAAAAU_XenlwdfrVZM-zuvc62nYHViLO7mKk5yL21F8iawCBuB86vDZfHLbXG8fpgZ1vl4GM1x63C2sk30r5LbZ_K1gzlF9NjPMQGW1n6KbxrVRoVhrjCNLBueG3alJS67p0REhBRwHdi9kZo1IKua5rUo7wcGhR_CuSWcza0bs8zlnn6zQzkYW40DA', True, ['Monday: Open 24 hours', 'Tuesday: Open 24 hours', 'Wednesday: Open 24 hours', 'Thursday: Open 24 hours', 'Friday: Open 24 hours', 'Saturday: Open 24 hours', 'Sunday: Open 24 hours'], 'favicon.ico'], ['Lansdowne Hotel', '27 -29 Pembroke Rd, Dublin 4, Ireland', 'http://www.lansdownehotel.ie/', 'CmRaAAAAUONsVeNoI1vx8kZdpZG4kr2-r0Hmlsh9zftFU_Jq0WDM_gaDvlFkYmiwF4ecFug5umgS4WebN93uOZwFCqy9YDqaDWesWL8uPASFUeiQFQo4_LYFa7XO0EfO-uR5zMl9EhAaW9Gu3_pgcD3XxqTK5-X3GhQ7cwUGQcfmgu_YNxg_W-sedEQR_w', 'empty', 'empty', 'favicon.ico'], ['Conrad Dublin', "Earlsfort Terracе, Saint Kevin's, Dublin 2, D02 V562, Ireland", 'http://conradhotels3.hilton.com/en/hotels/dublin/conrad-dublin-DUBHCCI/index.html?WT.mc_id=zELWAKN0EMEA1HI2DMH3LocalSearch4DGGenericx6DUBHCCI', 'CmRaAAAAC8a8ByaiF1jyYvFcNG54fzP9-c7TRhVHTPjlrz4inRA5EaNzx7aS7wGwt1EKwc8veMmaUtVVNw7rA5d1EbmQ5vxm6FDt6hzLVu-vcOy55W_y2SiX49M-5_eo7t9wZNi0EhAwphv7IEG6bgWebP3S7GwGGhR0tlPAvoes0o5hBs3L7QeU1tQZNw', 'empty', 'empty', 'favicon.ico'], ['The Merrion Hotel Dublin', 'Merrion Street Upper, Dublin 2, Ireland', 'http://www.merrionhotel.com/', 'CmRaAAAA2kgHZy3RK3N1rYd5EjNHYDBaUeyI73DV9U5wW9QKuN33Dnc8ETG64lIh_NOIX8yI4IzYQ2S16CmQwIudYbr_O_wc2EItQdHIpCos8fbGI7maoj-0wI69zTNUwC0fqAXiEhCTnk49jF_EVfopyngzdvd3GhRIITCbi3YV22ur53xmabEszWdpLg', True, ['Monday: Open 24 hours', 'Tuesday: Open 24 hours', 'Wednesday: Open 24 hours', 'Thursday: Open 24 hours', 'Friday: Open 24 hours', 'Saturday: 12:00 AM – 11:59 PM', 'Sunday: Open 24 hours'], 'favicon.ico'], ['Waterloo House', '10 Waterloo Rd, Dublin 4, Co. Dublin, D04 T651, Ireland', 'http://waterloohouse.ie/', 'CmRaAAAAhBydQj69zC36Cre62cvsN6bOILBu8ZfqDGkQnn_Mjrk2-qAC7ANTex9Mk2HyN_dmMeecjCM4BZ8ytFRudlAjxYLRB_rmXCvsnf_PzUnUSHJ0AFIfOsVmTuBb6jMtzqKhEhCc2aELCn506iYrKEZ7bU88GhTXZ2edjSciNKnmCdFDjxVSWyRquQ', 'empty', 'empty', 'favicon.ico'], ['Leeson Inn Downtown', "24 Lower Leeson Street, Saint Kevin's, Dublin, Ireland", 'http://www.leesoninndowntown.com/', 'CmRaAAAAsF5yqp5zatxao7cHASj-2u9ligYOt8ZlPXHX2kG8xyXuHsSD6HW_tbMUGzx6FB2Lxh3Qmqp9ZbkAJZ7XE415DQLuYZAdfEDywBKk7npA5ovEWkOT71rhwYAOw1jjjTTjEhB99O4y400myw-6jO4E_MJoGhQvMz8xxtS9W_KmV01rz49pUcxxvA', 'empty', 'empty', 'favicon.ico'], ['Clayton Hotel Burlington Road', 'Leeson Street Upper, Dublin, D04 A318, Ireland', 'https://www.claytonhotelburlingtonroad.com/', 'CmRaAAAAo08r5hQN9xvFJSPCXjirvurstPRbuiWyQljoXg_YNpUt_yWY_vHnv9MDuPbD8T-DhydBraOowAFiWw-lkScciKkN348wNzmO7lqY2q5udm32I7QmIiI6INfcIfYhBL6qEhDaujVeLvgk0FHYsMQEF40jGhQiyPUKxpmefLx8bn1JVGHWG84qhg', 'empty', 'empty', 'favicon.ico'], ['Leeson Apartments', '1 Leeson Street Upper, Dublin 4, D04 AH22, Ireland', 'https://www.leesonapartments.com/', 'empty', 'empty', 'empty', 'favicon.ico'], ['Harvest Moon Centre', '24 Baggot Street Lower, Dublin 2, D02 EW26, Ireland', 'http://www.harvestmoon.ie/', 'CmRZAAAAkAvqjM0QGNqRLsUBDBvrOs0z-sGEzzz8rimo6Jgv2ePBSxFe7PZLx1Rl-ZdVprcv_bsBC4Gx_xYf3VZc_dCSIpiq_H6DjLZUFoswhjovkPsJXNzV8S_GQCDK4mXYUYxvEhBIgZOmEUjmI3_4tQbsCrLbGhTZfyE6UhyOnz6khKROsEVv4nI8KQ', False, ['Monday: 10:00 AM – 9:00 PM', 'Tuesday: 10:00 AM – 9:00 PM', 'Wednesday: 10:00 AM – 9:00 PM', 'Thursday: 10:00 AM – 9:00 PM', 'Friday: 10:00 AM – 9:00 PM', 'Saturday: 11:00 AM – 8:00 PM', 'Sunday: 11:00 AM – 7:00 PM'], 'favicon.ico'], ['Matt The Thresher', '31-32 Pembroke Street Lower, Dublin 2, Ireland', 'http://mattthethresher.ie/', 'CmRaAAAAk_lNXu8nEp3xDuqe3QMuMLUZf0qmIroj_cAxde3NMPr80xAEnmcJZu5AmPYBDBkuaQs1BLgWucr2pjt_0pSAIa3a5A_nUA_5-h3FsBaEu_cZfN45B6g_R8WkumPzI8cSEhAqFn771qI-kYU4TeqZcgOSGhRrCRE0_nuU3AeEdxeSpZXZiz5tqQ', False, ['Monday: 10:00 AM – 9:45 PM', 'Tuesday: 10:00 AM – 9:45 PM', 'Wednesday: 10:00 AM – 9:45 PM', 'Thursday: 10:00 AM – 9:45 PM', 'Friday: 10:00 AM – 9:45 PM', 'Saturday: 12:00 – 9:45 PM', 'Sunday: 12:30 – 8:30 PM'], 'favicon.ico'], ['Toners', '139 Baggot Street Lower, Dublin 2, Ireland', 'http://www.tonerspub.ie/', 'CmRaAAAAM91LaHTDMG6hixlodamrpnXx8u9CicpOfAmn73hKZl99BN9lY3G1lI5xxsWe2KrVn8ssHlOBdxzqFpzRNOMKr5yAs6NztY1HGFMwv3BwFU7DPNo12L4F3MWnF_PXPH8jEhAQMRR5AVWk-kU_rj45myQJGhSyE6e33pY5MuT-H9jSbbpM4zNmbg', True, ['Monday: 10:30 AM – 11:30 PM', 'Tuesday: 10:30 AM – 11:30 PM', 'Wednesday: 10:30 AM – 11:30 PM', 'Thursday: 10:30 AM – 11:30 PM', 'Friday: 10:30 AM – 12:30 AM', 'Saturday: 10:30 AM – 12:30 AM', 'Sunday: 11:30 AM – 11:30 PM'], 'favicon.ico'], ['Blow Salons', '144 Leeson Street Upper, Dublin, D04 Y564, Ireland', 'http://www.blow.ie/?utm_source=GMBlisting&utm_medium=Organic', 'CmRaAAAAb_UQSzUnQqne392ss-IbD5uINtI_BH1VAK2lQWVVVL_da-lF7i_ZTucECXPqYCIe3jyn5tFIHcDgOSXxVjGKXnqwbnGLNO-TzJwakB9UFLBn2uVK_pXDhHxjsL1zI0doEhDRIeetgqB7Q_Hhz4FrrC15GhRvsD1IIRYHLupHG1ahkxwKxgo3vQ', False, ['Monday: 6:45 AM – 7:30 PM', 'Tuesday: 6:45 AM – 7:30 PM', 'Wednesday: 6:45 AM – 7:30 PM', 'Thursday: 6:45 AM – 7:30 PM', 'Friday: 6:45 AM – 7:30 PM', 'Saturday: 9:00 AM – 6:00 PM', 'Sunday: 10:00 AM – 4:00 PM'], 'favicon.ico'], ['Active Physiotherapy and Acupuncture Clinic', '112c Lower Baggot Street, Dublin 2, Grand Canal Dock, Dublin, Co. Dublin, Ireland', 'empty', 'empty', False, ['Monday: 8:30 AM – 6:00 PM', 'Tuesday: 8:30 AM – 7:00 PM', 'Wednesday: 8:30 AM – 6:00 PM', 'Thursday: 8:30 AM – 7:30 PM', 'Friday: 8:30 AM – 6:00 PM', 'Saturday: Closed', 'Sunday: Closed'], 'favicon.ico'], ['Cpl Resources Plc', '8-, 34 Percy Pl, Dublin 4, Ireland', 'http://www.cpl.ie/', 'CmRaAAAAHOz8xDJoDXTMLDyMkw_bft3vIT70CB1bi-HRveLQOzcGtnATJNMcFh_mQdXuU4zsn87K6z7A21zHvtTRRPHQH5WVa8RwpyXhgIeRXZjlLco2z6VUK5O0AbVHoe288Zj5EhBltRXuzef7RhHlqR7Rsd9EGhTcKGyMrKuyRu7azeFqi3Di4DkKBg', False, ['Monday: 9:00 AM – 5:30 PM', 'Tuesday: 9:00 AM – 5:30 PM', 'Wednesday: 9:00 AM – 5:30 PM', 'Thursday: 9:00 AM – 5:30 PM', 'Friday: 9:00 AM – 5:30 PM', 'Saturday: Closed', 'Sunday: Closed'], 'favicon.ico'], ['Chez Max - Baggot St', '133 Lower Baggot St, Dublin 2, Co. Dublin, Ireland', 'http://www.chezmax.ie/baggot/', 'CmRaAAAAfvArhJsgqzqB_F0QIlpsYcqA-45bZf0fMV0jooDv60JbfU5V4ZIg5m9pDTWGOhnzQUVIIObDL2GOzCWreKFcuixaoT2j_4_WZ3ZoToo_6IWJ2hS1ngM_kNzd6zMxQ0qeEhCM-65t30nCwwK6zLs1mXOqGhScgjXSvCDfeAIKha5GmxhonVJW1g', True, ['Monday: 12:00 – 3:30 PM, 5:30 – 10:00 PM', 'Tuesday: 12:00 – 3:30 PM, 5:30 – 10:00 PM', 'Wednesday: 12:00 – 3:30 PM, 5:30 – 10:00 PM', 'Thursday: 12:00 – 3:30 PM, 5:30 – 10:00 PM', 'Friday: 12:00 – 3:30 PM, 5:30 – 11:00 PM', 'Saturday: 11:00 AM – 4:00 PM, 5:30 – 11:00 PM', 'Sunday: Closed'], 'favicon.ico'], ['KD Media', '5 Fitzwilliam Pl, Grand Canal Dock, Dublin, Ireland', 'http://www.kinkydevil.ie/', 'empty', 'empty', 'empty', 'favicon.ico'], ['Abbeyleigh House', 
	# '28 Leeson Street Upper, Dublin 4, D04 XF72, Ireland', 'https://abbeyleighhouse.wordpress.com/', 'CmRaAAAAd4Wqvz7eF9BUnxD6m_WhfK4U095z2IyivfTKVNy8d8nxUsdwPU1iNL_MjL4y4czRYUliTWUp4l7TPZDCVTbkONcdBgBIsfv8xwkwGDBMgoHA9F1f2VjjQ3n4-_etv5gGEhDqI5tWwhqZbiKTUImg_831GhQGutZb0xxnnCn-IfKcQW8qn8dT-g', 'empty', 'empty', 'favicon.ico'], ['Rathmines', 'Rathmines, Co. Dublin, Ireland', 'empty', 'CmRaAAAAGbpSdH2x8ieTsxwrvs5mF9UmlJF2KlaIj3E1BeMyJTN4EhL6SiAIbTRgfDDfTjRJnK4x3jmqrca9X3iY9EXnvUF3QHhOLtlAuoSEe03YYTkVH8Dw5vpwzsisvfr6FE7QEhDkpu0H-pmciaC0Nsp98P-bGhTiK6PomVGEQxYs7De2JMh9P6A9sg', 'empty', 'empty', 'favicon.ico']]
	
	# return total_results
	
	try:

		URL = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
				+ coordinates+'&radius=500&key='+api_key+'&type='+place_type)
		r = requests.get(URL)
		response = r.text
		python_object = json.loads(response)
		results = python_object['results']
		for result in results:
			place_name = result['name']
			place_id = result['place_id']
			place_address_website_image=[]
			place_address_website_image.append(get_place_image_address_website(place_id))
			if place_name is not None and place_address_website_image is not None:
				if place_address_website_image[0][0][0] is not None:
					place_address = place_address_website_image[0][0][0]
				else:
					place_address ='empty'
				if place_address_website_image[0][0][1] is not None:
					place_website = place_address_website_image[0][0][1]
				else:
					place_website = 'empty'
				if place_address_website_image[0][0][2] is not None:
					place_image = place_address_website_image[0][0][2]
				else:
					place_image ='empty'
				if place_address_website_image[0][0][3] is not None:
					place_opening_hours = place_address_website_image[0][0][3]
				else:
					place_opening_hours = 'empty'
				if place_address_website_image[0][0][4] is not None:
					place_program = place_address_website_image[0][0][4]
				else:
					place_program = ' empty'

				total_results.append([place_name, place_address, place_website, place_image, place_opening_hours, place_program, place_type])
	except:
		print("error trying to search palces")
		return 
	# try:
	# 	next_page_token = python_object['next_page_token']
	# except KeyError:
	# 	# no next page
	# 	print('Key Error')
	# 	return
	# time.sleep(1)
	# get_nearby_places(coordinates, place_type, next_page_token)
	# print(total_results)
	return total_results


def get_place_image_address_website(place_id):

	try:
		reqURL = ('https://maps.googleapis.com/maps/api/place/details/json?placeid='
			+ place_id+'&key='+api_key)
		r = requests.get(reqURL)
		
		response = r.text
		python_object = json.loads(response)
		# place_image = []
		place_attr = []
		
		place_details = python_object["result"]
		# get photo ref
		if 'photos' in place_details:
			place_image = place_details['photos'][0]['photo_reference']
		else:			
			place_image = 'empty'

		#get website
		if 'website' in place_details  and place_details['website'] is not None:
			place_website = place_details['website']
		else:
			place_website = 'empty'

		

		# get place address
		if 'formatted_address' in place_details and place_details['formatted_address'] is not None:
			place_address = place_details['formatted_address']
		elif 'adr_address' in place_details and  place_details['adr_address'] is not None:
			place_address = place_details['adr_address']
		else:
			place_address = 'empty'

		# get place opening_hours
		if 'opening_hours' in place_details and place_details['opening_hours'] is not None:
			if 'open_now' in place_details['opening_hours']:
				place_opening_hours = place_details['opening_hours']['open_now']
			else:
				place_opening_hours = 'empty'
			if 'weekday_text' in place_details['opening_hours']:
				place_weekday_text = place_details['opening_hours']['weekday_text']
			else:
				place_weekday_text = 'empty'
		else:
			place_opening_hours = 'empty'
			place_weekday_text = 'empty'
		place_attr.append([place_address, place_website, place_image, place_opening_hours, place_weekday_text])
		return place_attr
	except:
		print("err getting place details")
		return
# get outdoor places based on coordinates
def get_outdoor_places(coordinates):
	outdoor_places = []
	try:
		for outdoor_category in outdoor_categories.keys():
			# print(outdoor_category)
			outdoor_places.extend(get_nearby_places(coordinates, outdoor_category, ''))
			# outdoor_places.append(places_by_category)
	except:
		print("cannot get outdoor places")
		return
	# print(outdoor_places)
	return outdoor_places

# get indoor places based on coordinates
def get_indoor_places(coordinates):
	indoor_places = []

	try:
		for indoor_category in indoor_categories.keys():
			# print(coordinates)
			# print(get_nearby_places(coordinates, indoor_category, ''))
			indoor_places.extend(get_nearby_places(coordinates, indoor_category, ''))
			# print(indoor_places)
			# indoor_places.append(places_by_category)
	except:
		print("cannot get indoor places")
		return
	# print(indoor_places)
	return indoor_places

# get_nearby_places(my_coordinates(), 'park', '')

# print(total_results)
