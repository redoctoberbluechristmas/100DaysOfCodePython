import requests
from datetime import datetime

MY_LAT = 47.63373423745527
MY_LONG = -122.13531681500972

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise']
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunrise_minute = sunrise.split("T")[1].split(":")[1]
sunrise_second = sunrise.split("T")[1].split(":")[2].split("+")[0]

sunset = data['results']['sunset']
sunset_hour = sunset.split("T")[1].split(":")[0]
sunset_minute = sunset.split("T")[1].split(":")[1]
sunset_second = sunset.split("T")[1].split(":")[2].split("+")[0]

#print(sunrise) # ---> 2021-04-27T12:55:52+00:00
#print(sunrise.split("T")) # ---> ['2021-04-27', '12:55:52+00:00']
#print(sunrise.split("T")[1]) # ---> 12:55:52+00:00
#print(sunrise.split("T")[1].split("+")) # ---> ['12:55:52', '00:00']
#print(sunrise.split("T")[1].split("+")[0]) # ---> 12:55:52
#print(sunrise.split("T")[1].split(":")[0]) # --> gives hour 12
#print(sunrise.split("T")[1].split(":")[1]) # ---> gives minute 55
#print(sunrise.split("T")[1].split(":")[2].split("+")[0]) # --> gives second 52


print(sunrise_hour)
print(sunset_hour)

time_now = datetime.now()
print(time_now.hour)