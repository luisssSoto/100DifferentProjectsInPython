#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from dotenv import load_dotenv
import requests
from pprint import pprint
import datetime

from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

load_dotenv()
api_key_sheety = os.getenv("API_KEY_SHEETY")
print(f"api sheety: {api_key_sheety}")
header_sheety = {
    "Authorization": f"Basic {api_key_sheety}"
}

get_sheety_endpoint = "https://api.sheety.co/c12db56504563295f7629b0fbf1c32d5/flightDeals/prices"
response = requests.get(url=get_sheety_endpoint, headers=header_sheety)
response.raise_for_status()
print(response.text)
print(response)
sheet_data = response.json()["prices"]
print(f"sheet data: {sheet_data}")
pprint(sheet_data)

flight_search = FlightSearch(sheet_data)
flight_search.get_iata_code()

data_manager = DataManager(sheet_data)

put_sheety_endpoint = get_sheety_endpoint + "/"
data_manager.modify_sheet(endpoint=put_sheety_endpoint, header=header_sheety)

flight_data = FlightData()
flight_data.origin_location_code = "LON"

departure_date = datetime.datetime.now() + datetime.timedelta(days = 1)
departure_date.strftime("%Y-%m-%d")
return_date = departure_date + datetime.timedelta(days = 30 * 6)
return_date = return_date.strftime("%Y-%m-%d")
departure_date = str(departure_date)[:10]

for city in sheet_data:
    flight_data.destination_location_code = city["iataCode"]
    flight_data.departure_date = departure_date
    flight_data.return_date = return_date
    flight_data.adults = 1
    flight_data.non_stop = "true"
    flight_data.currency_code = "GBP"
    bargain_flight = flight_data.find_cheapest_flight()
    notification_manager = NotificationManager(bargain_flight)
    notification_manager.send_msg(city["lowestPrice"])