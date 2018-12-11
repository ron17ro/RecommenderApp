Weather Recommendation App
==============

Purpose of the Weather Recommendation App
--------------
The purpose of this app is to provide the user with a list of recommended activities based on the current weather at their location.
The user's location is determined by their IP browser.
The app offers a list of activities within a 500-meter radius from the user's location from a list of categories specified in place.py, either from the dictionary outdoor_categories[] or
in the dictionary indoor_categories[], depending on the current weather
The app also offers the possibility for the user to choose from a range of categories and display the relevant categories within the radius (regardless of the weather).

Technologies used
--------------
**Front-end**
- HTML
- CSS
- Bootstrap framework for CSS

**Back-end**
- Python
- Flask Framework

**APIs:** 
- ipinfo.io to find the user's ip address
- Open Weather Map to find the weather at a given location
- Google Places to get a list of places based on the location
- Mailgun to send the any user's comment to the moderator of the website

**Deployment**
- The Weather Recommendation App is deployed on Heroku
- Config variables have been used to maintain the security of the API keys
- The application can be set to work on local if the following:
	- in location.py use the code block inside "#use this to test on local"  and comment the block specified by "# # use this on heroku to get the IP on the client(remote addr), if used to run the app on local it will return 127.0.0.1"
	- in location.py, MainProgram.py, weather.py, places.py, the import section uses the line specified by "# use settings.py on local" and should comment the line specified by "# use keys.py on heroku"
	- an additional settings.py is creating containing your API KEYS
	KEYS =dict([
		('OpenWeatherMap', 'yourkey'),
		('google_API', 'yourkey'),
		('mailGun': 'yourKey'),
		('CommentEmail':  'an email address where to send the feedback from the contact page')

])


Future Features/Improvements
--------------

**Future Features**
- Twitter feed displaying tweets based on the location and weather with the use of hashtags (for example, #Dublin and #rain)(currently the search by hashtag widget is discontinued. The REST Search API can be used to search timelines, however, a display interface has to be written from scratch according to this article: 
https://twittercommunity.com/t/deprecating-widget-settings/102295)
- Extra places offerings not only based on the weather but on place categories the user is interested in, for example "clothing store" or "spa". This feature is partially implemented through the list of place categories displayed at the top.


**Design Improvements**
- Create a "mega-menu" for the list of place categories (currently place in the jumbotron)
- General layout work 
- The Twitter feed described above would be placed on the right-hand side of the website
- Use JQuery to retrieve places instead of Python

**Limitation**
- It doesn't work with clients using a VPN connections. The geolocation API returns an empty city .

