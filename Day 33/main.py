import requests
import datetime
import smtplib
from dotenv import load_dotenv
import os
import time

MY_LAT = 29.232723
MY_LNG = -98.500230

my_position = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

my_location = requests.get(" https://api.sunrise-sunset.org/json", my_position,)
my_location.raise_for_status()
my_location = my_location.json()
sunrise = my_location["results"]["sunrise"]
sunset = my_location["results"]["sunset"]

sunrise = float(sunrise[11:13])
sunset = float(sunset[11:13])


def is_iss_near():
    if my_position["lat"] - 5 <= iss_lat <= my_position["lat"] + 5 and my_position["lng"] - 5 <= iss_lng <= my_position["lng"] + 5:
        return True
    return False

def is_dark():
    now = datetime.datetime.now()
    if sunset < now.hour < sunrise:
        return True
    else:
        return False

load_dotenv()
from_email = os.getenv("FROM_EMAIL")
password = os.getenv("MY_PASSWORD")
to_email = os.getenv("TO_EMAIL")

while True:
    iss_data = requests.get("http://api.open-notify.org/iss-now.json")
    iss_data.raise_for_status()
    iss_data = iss_data.json()
    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    if is_iss_near() is True and is_dark() is True:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=from_email, password=password)
            connection.sendmail(from_addr=from_email, to_addrs=to_email,
                                msg=f"Subject:Look up on the sky\n\nHi the ISS is on top of us!")
    print(iss_lat, iss_lng)
    print(is_iss_near(), is_dark())
    time.sleep(60)
