import os
from dotenv import load_dotenv

load_dotenv()

from_email = os.getenv('FROM_EMAIL')
to_email = os.getenv('TO_EMAIL')
my_password = os.getenv('MY_PASSWORD')

import smtplib

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=from_email, password=my_password)
    connection.sendmail(from_addr=from_email,
                        to_addrs=to_email,
                        msg=f"Subject:Test\n\nWould you mind if use your email for my tests?")
