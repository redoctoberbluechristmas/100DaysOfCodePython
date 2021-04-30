import requests
import smtplib
import sched
import time
from datetime import datetime

MY_EMAIL = "<someemail>"
PASSWORD = "<somepassword>"
TO_EMAIL = "<someotheremail>"
MY_LAT = mylat # Your latitude as float
MY_LONG = mylong # Your longitude as float

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def check_daylight_savings():
    is_daylight_savings = time.localtime().tm_isdst
    return is_daylight_savings


def time_zone_conversion(time):  #<---- pass ISS time results here
    if check_daylight_savings() == 1:
        tz_diff = 7
    else:
        tz_diff = 8

    converted_time = time - tz_diff
    if converted_time < 0:
        converted_time += 12
    return converted_time



def check_if_night(current_time, my_position):
    sunset_response = requests.get("https://api.sunrise-sunset.org/json", params=my_position)
    sunset_response.raise_for_status()
    sunset_data = sunset_response.json()
    sunrise = int(sunset_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sunset_data["results"]["sunset"].split("T")[1].split(":")[0])

    print(sunrise)
    print(sunset)

    converted_sunrise = time_zone_conversion(sunrise)
    converted_sunset = time_zone_conversion(sunset)


    if converted_sunset < 13:
        converted_sunset += 12

    print(f"Current time is {current_time}")
    print(f"Converted sunrise is {converted_sunrise}")
    print(f"Converted sunset is {converted_sunset}")

    if current_time < converted_sunrise and current_time < converted_sunset:
        return True
    else:
        return False


def compare_position(my_position, iss_lat, iss_long):
    my_lat = my_position['lat']
    my_lng = my_position['lng']

    lat_diff = (my_lat - iss_lat)
    lng_diff = (my_lng - iss_long) * -1
    if lat_diff < 5 and lng_diff < 5:
        return True
    else:
        return False


def check_iss():
    time_now = datetime.now()
    time_now = int(time_now.strftime("%H"))

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    #Your position is within +5 or -5 degrees of the ISS position.
    if compare_position(parameters, iss_latitude, iss_longitude) and check_if_night(time_now, parameters):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg=f"Subject: Space Station Overhead\n\nSpace station is overhead."
            )
    else:
        print("Nowhere close")
    s.enter(60, 1, check_iss)


s = sched.scheduler(time.time, time.sleep)
s.enter(60, 1, check_iss)
s.run()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


