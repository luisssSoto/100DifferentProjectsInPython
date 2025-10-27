import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, data):
        self.data = data
        self.row_endpoint = 2
    def modify_sheet(self, endpoint, header):
        for i in range(len(self.data)):
            print(self.data[i]["iataCode"])
            prices = {
                "price": {
                    "iataCode": self.data[i]["iataCode"],
                }
            }
            response = requests.put(url=endpoint + str(self.row_endpoint), json=prices, headers=header)
            response.raise_for_status()
            self.row_endpoint += 1



