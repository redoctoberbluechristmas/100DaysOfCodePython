import os
import requests
from twilio.rest import Client

OWM_WEATHER_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather"
OWM_ONE_CALL_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

CITY_NAME = "Redmond"
STATE_CODE = "WA"
COUNTRY_CODE = "US"
API_KEY = os.getenv('OWM_API_KEY')
LAT = 47.6336
LONG = -122.1354
EXCLUDE_LIST = "current,minutely,daily" # Don't need this, cut it to save time/bandwidth

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
twilio_client = Client(account_sid, auth_token)


# request_parameters = {
#         "q": f"{CITY_NAME},{STATE_CODE},{COUNTRY_CODE}",
#         "appid": API_KEY,
# }

# # API Call 1
# I included this because I wanted a way to get lat/long from city/state/country, but I was making two calls for
# something I easily could find from Google so I commented it out for now.

# response = requests.get(OWM_WEATHER_ENDPOINT, params=request_parameters)
# response.raise_for_status()
# print(response.status_code)
# data = response.json()
#
# #print(data)
#
# lat = data['coord']['lat']
# lon = data['coord']['lon']



one_call_request_parameters = {
        "lat": LAT,
        "lon": LONG,
        "appid": API_KEY,
        "exclude": EXCLUDE_LIST
}


#OneCall API
response = requests.get(OWM_ONE_CALL_ENDPOINT, params=one_call_request_parameters)
response.raise_for_status()
weather_data = response.json()

# Slice weather data to get only first 12 hours
first_12_hours = weather_data['hourly'][:12]

will_rain = False

# Get weather id for first 12 hours
for i in first_12_hours:
    chance_of_precip = i['pop']
    if chance_of_precip > 0.59:
        will_rain = True
        # id = i['weather'][0]['id']
        # if id < 700:
        #     print("Bring an umbrella")
        # elif id == 804:
        #     print("It will be overcast.")

if will_rain:
    print("Bring an umbrella")
    message = twilio_client.messages.create(
        body="It will rain today. Bring an umbrella.",
        from_="+12092942007",
        to="+17604928126"
    )

    print(message.status)