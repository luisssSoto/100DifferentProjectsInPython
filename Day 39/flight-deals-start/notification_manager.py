import requests
import os
import dotenv
from twilio.rest import Client

dotenv.load_dotenv()

account_sid= os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, bargain_flight):
        self.__account_sid = account_sid
        self.__auth_token = auth_token
        self.bargain_flight = bargain_flight

    def send_msg(self, sheet_price):
        if len(self.bargain_flight) > 0:
            msg = ""
            if self.bargain_flight[0] < sheet_price:
                msg += f"Low price alert! Only £{self.bargain_flight[0]} to fly from {self.bargain_flight[1]} to {self.bargain_flight[2]} on {self.bargain_flight[3]} to {self.bargain_flight[4]}"
                print(msg)
                client = Client(self.__account_sid, self.__auth_token)
                message = client.messages.create(
                    from_="whatsapp:+14155238886",
                    body=msg,
                    to=f"whatsapp:{os.getenv('TEL_NUMBER')}"
                )
                print(f"body: {message.body}")
        else:
            print("There is no flights")


