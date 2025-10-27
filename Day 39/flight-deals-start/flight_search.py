import os
import dotenv
import requests

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
CITY_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

dotenv.load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, data):
        self.flight_data = data
        self.__api_key = os.environ["API_KEY_AMADEUS"]
        self.__api_secret = os.environ["API_SECRET_AMADEUS"]
        self.__token = self.get_new_token()

    def get_new_token(self):
        self.head = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        self.params = {
            "grant_type": "client_credentials",
            "client_id": self.__api_key,
            "client_secret": self.__api_secret
        }

        response = requests.post(url=TOKEN_ENDPOINT, data=self.params, headers=self.head)
        response.raise_for_status()
        print(response)
        data = response.json()
        print(data)
        token = data["access_token"]
        print(token)
        return token

    def get_iata_code(self):
        head = {
            "Authorization": f"Bearer {self.__token}",
        }
        params = {
            "keyword": "",
        }
        for city in self.flight_data:
            if city["iataCode"] == "":
                params["keyword"] = city["city"]
                print(f"name of city: {city['city']}")
                print(f"parameters: {params}")
                response = requests.get(url=CITY_ENDPOINT, params=params, headers=head)
                response.raise_for_status()
                data = response.json()
                iata_code = data["data"][0]["iataCode"]
                city["iataCode"] = iata_code



