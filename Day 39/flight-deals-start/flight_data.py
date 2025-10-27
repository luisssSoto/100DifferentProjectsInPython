import requests
import os
import dotenv

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"


dotenv.load_dotenv()

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.origin_location_code = None
        self.destination_location_code = None
        self.departure_date = None
        self.return_date = None
        self.adults = None
        self.non_stop = None
        self.currency_code = None

        self.__api_key = os.environ["API_KEY_AMADEUS"]
        self.__api_secret = os.environ["API_SECRET_AMADEUS"]
        self.__token = self.get_new_token()

    def get_new_token(self):
        head = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": self.__api_key,
            "client_secret": self.__api_secret
        }

        response = requests.post(url=TOKEN_ENDPOINT, data=data, headers=head)
        response.raise_for_status()
        print(response)
        data = response.json()
        print(data)
        token = data["access_token"]
        print(token, " 2")
        return token

    def find_cheapest_flight(self):
        head = {
            "Authorization": f"Bearer {self.__token}",
        }
        params = {
            "originLocationCode": self.origin_location_code,
            "destinationLocationCode": self.destination_location_code,
            "departureDate": self.departure_date,
            "returnDate": self.return_date,
            "adults": self.adults,
            "nonStop": self.non_stop,
            "currencyCode": self.currency_code
        }
        response = requests.get(url=FLIGHT_ENDPOINT, params=params, headers=head)
        response.raise_for_status()
        print(f"response: {response}")
        data = response.json()
        # print("last data:", data)
        cheapest_price = float('inf')
        print(f"length of data: {len(data)}")
        bargain_data = []
        for offer in data["data"]:
            price = float(offer["price"]["grandTotal"])
            if price < cheapest_price:
                cheapest_price = price
                offer_id = offer["id"]
                print(f"departure: {self.origin_location_code} and arrival: {self.destination_location_code}")
                print(f"cheapest price: {price} and offer_id: {offer_id}")
                bargain_data = [cheapest_price, self.origin_location_code, self.destination_location_code, self.departure_date, self.return_date]
        return bargain_data