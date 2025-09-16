##################### Extra Hard Starting Project ######################
import os
from dotenv import load_dotenv

load_dotenv()
from_email = os.getenv("FROM_EMAIL")
my_password = os.getenv("MY_PASSWORD")

# 1. Update the birthdays.csv
import pandas
df = pandas.read_csv('birthdays.csv')
df = df.to_dict(orient='records')

# 2. Check if today matches a birthday in the birthdays.csv
import datetime
import random
dt = datetime.datetime.now()
for row in df:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    if row["month"] == dt.month and row["day"] == dt.day:
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path, "r") as letter:
            letter_list = letter.readlines()
        first_row = letter_list[0].replace("[NAME]", row["name"])
        last_row = letter_list[-1].replace("Angela", "Alex")
        letter_list[0] = first_row
        letter_list[-1] = last_row
        final_letter = "".join(letter_list)
# 4. Send the letter generated in step 3 to that person's email address.
        import smtplib
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=from_email, password=my_password)
            connection.sendmail(from_addr=from_email, to_addrs=row["email"], msg=f"Subject:Happy Birthday!\n\n{final_letter}")


