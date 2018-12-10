Weather Recommendation App
==============

Purpose of the Weather Recommendation App
--------------
The purpose of this app is to provide the user with a list of recommended activities based on the current at their location.
The user's location is determined by their IP browser.
The app offers a list of activities within a 700-meter radius from the user's location.
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

**Deployement**
The Weather Recommendation App is deployed on Heroku
Config variables have been used to maintain the security of the API keys

Future Features/Improvements
--------------

**Futures Features**
- Twitter feed displaying tweets based on the location and weather with the use of hashtags (for example, #Dublin and #rain)
- Extra places offerings not only based on the weather but on place categories the user is interested in, for example "clothing store" or "spa". This feature is partially implemented through the list of place categories displayed at the top.


**Design Improvements**
- Create a "mega-menu" for the list of place categories (currently place in the jumbotron)
- General layout work 
- The Twitter feed described above would be placed on the right-hand side of the website

Current issues
--------------

We faced some issues deploying the app to Heroku. While the app is up and running in Heroku, the functionality to display the recommended places does not work expected.
This functionality works well on a local environment and after spending some time troubleshooting the issue, we assume it might be a limitation of the API keys.
Due to time constraints, we chose to leave it as it on Heroku for the moment.
 