"""Passing Parameters To API"""
import requests

LAT = 26.192566
LNG = -98.184608

coordinates = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}
data = requests.get("https://api.sunrise-sunset.org/json",coordinates,)
data.raise_for_status()

# Deserialization
data = data.json()
print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise, sunset)
sunrise = sunrise[11:19]
sunset = sunset[11:19]
print(sunrise, sunset)
sunrise_hour = sunrise[0:2]
sunset_hour = sunset[0:2]

from datetime import datetime

today = datetime.now()
print(sunrise_hour)
print(sunset_hour)
print(today.hour)