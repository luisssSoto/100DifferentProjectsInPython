import smtplib
import random
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

from_email = os.getenv('FROM_EMAIL')
to_email = os.getenv('TO_EMAIL')
my_password = os.getenv('MY_PASSWORD')

today = datetime.datetime.now()
weekday = today.weekday()

if weekday == 0:
    with open("quotes.txt", "r") as quotes:
        quotes_list = quotes.readlines()

    random_quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(from_email, my_password)
        connection.sendmail(from_email, to_email, f"Subject: Motivational Quote\n\n{random_quote}")
