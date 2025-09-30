from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client

load_dotenv()
api_key = os.getenv('API_KEY')
lat = os.getenv('MY_LAT')
lng = os.getenv('MY_LNG')

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

weather_params = {
    "lat": lat,
    "lon": lng,
    "cnt": 4,
    "appid": api_key
}

weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
response = requests.get(weather_endpoint, params=weather_params)

response.raise_for_status()
print(f"status: {response}")
data = response.json()
print(f"data: {data}")
weather_id = data["list"][0]["weather"][0]["id"]
print(f"weather id: {weather_id}")
weather_description = data["list"][0]["weather"][0]["description"]
print(f"weather description: {weather_description}")


def may_rain(id):
    if id < 700:
        return True
    else:
        return False

for i in range(data["cnt"]):
    weather_id = data["list"][i]["weather"][0]["id"]
    if may_rain(weather_id):
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body="it's going to rain today.Remember to bring an ☔",
            to=f"whatsapp:{os.getenv('TEL_NUMBER')}"
        )
        break
