import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from pprint import pprint

# Load environment variables from .env file
load_dotenv()

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._sheety_prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self._sheety_users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        print(f"user_name: {self._user}, password: {self._password}")
        self._header_sheety = {
            "Authorization": f"Basic {os.environ["API_KEY_SHEETY"]}"
        }
        print(f"header_sheety: {self._header_sheety}")
        # self._authorization = HTTPBasicAuth(self._user, self._password)
        # print(f"authorization: {self._authorization.raise_}")
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=self._sheety_prices_endpoint, headers=self._header_sheety)
        data = response.json()
        print(f"data: {data}")
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self._sheety_prices_endpoint}/{city['id']}",
                json=new_data,
                headers=self._header_sheety
            )
            print(f"response text: {response.text}")

    def get_customer_emails(self):
        response = requests.get(url=self._sheety_users_endpoint, headers=self._header_sheety)
        response.raise_for_status()
        data = response.json()
        print("get customer emails method")
        pprint(data)
        return data


