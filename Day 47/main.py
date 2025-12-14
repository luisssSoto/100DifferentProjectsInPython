# Approach 1: BeautifulSoup
from bs4 import BeautifulSoup
import requests

header = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language": "en-US,en;q=0.9,es-US;q=0.8,es;q=0.7",
"Priority": "u=0, i",
"Sec-Ch-Ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
"Sec-Ch-Ua-Mobile": "?0",
"Sec-Ch-Ua-Platform": "\"Windows\"",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "cross-site",
"Sec-Fetch-User": "?1",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
}


URL = "https://www.amazon.com.mx/Super-Mario-Wonder-Nintendo-Switch/dp/B0C93HKZ2T/ref=sr_1_5?__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1UOEFTHHZPPLB&dib=eyJ2IjoiMSJ9.0qWkj5swlTNlZlcpke9XhAo-eos_Mi5sKPhgGfwhBVvVEJ8vYx7EzHUenlw8XSOuYKzaeZh1dO6eLD0HSVPyEkV6qOZj9AenmPdG-94eh43_2_278KgLe8r2qEUslvFqD5B24lIoMAWwi_FLsKkPv6UkcmY5ZKAM6D47IJjZgqpk8SD6SIOnZA1hwRX33p9YjGA9gelFFwCndZeGjfj1V0W_2gQ4tAiklkioPwW5hNgCDJHp7GuRhrcbJUfJnw8I-qLI72xxFFMEX0AjV4fRteFBkR4bA2hZYmJlpWVRYh8.EPeUOJ85GxQM2QWVdZFVaASlhvvHOJ57a6CwZGoEcpc&dib_tag=se&keywords=mario+bros+switch&qid=1764853093&sprefix=mario+bros+switch%2Caps%2C161&sr=8-5&ufe=app_do%3Aamzn1.fos.03979ec5-04c0-4e2b-b2cb-0da67477c2a5"
response = requests.get(url=URL, headers=header)
response.raise_for_status()


bs = BeautifulSoup(response.text, "html.parser")
price = bs.select(selector="div #corePriceDisplay_desktop_feature_div span .a-price-whole")
price = float(price[0].getText())
product_name = bs.select(selector="span#productTitle")
product_name = product_name[0].getText().strip()
print(f"price: {price}")
print(f"name: {product_name}")

from smtplib import SMTP
from dotenv import load_dotenv
import os

load_dotenv()
email_address = os.getenv("EMAIL_ADDRESS")
amazon_password = os.getenv("AMAZON_TRACKER_PASSWORD")
smtp_address = os.getenv("SMTP_ADDRESS")


def send_email(smtp: str, from_email: str, to_email: str, password: str)-> None:
    try:
        with SMTP(host=smtp_address, port=587) as connection:
            connection.starttls()
            connection.login(user=email_address, password=password)
            connection.sendmail(from_addr=email_address, to_addrs=email_address, msg=f"Subject:Amazon Price Alert!\n\nThe product: {product_name} which have you been lookin forward is: {price}, just take a look: {URL}")
            print("The email was sent successfully")
    except BaseException as e:
        print(f"Something happend: {e}")

if float(price) < 800:
    send_email(smtp_address, email_address, email_address, amazon_password)
else: 
    print(f"The price of the product: {product_name} is still high: {price}")


# Approach 2: Selenium
from selenium import webdriver  
from selenium.webdriver.common.by import By

URL = "https://www.amazon.com.mx/Super-Mario-Wonder-Nintendo-Switch/dp/B0C93HKZ2T/ref=sr_1_5?__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1UOEFTHHZPPLB&dib=eyJ2IjoiMSJ9.0qWkj5swlTNlZlcpke9XhAo-eos_Mi5sKPhgGfwhBVvVEJ8vYx7EzHUenlw8XSOuYKzaeZh1dO6eLD0HSVPyEkV6qOZj9AenmPdG-94eh43_2_278KgLe8r2qEUslvFqD5B24lIoMAWwi_FLsKkPv6UkcmY5ZKAM6D47IJjZgqpk8SD6SIOnZA1hwRX33p9YjGA9gelFFwCndZeGjfj1V0W_2gQ4tAiklkioPwW5hNgCDJHp7GuRhrcbJUfJnw8I-qLI72xxFFMEX0AjV4fRteFBkR4bA2hZYmJlpWVRYh8.EPeUOJ85GxQM2QWVdZFVaASlhvvHOJ57a6CwZGoEcpc&dib_tag=se&keywords=mario+bros+switch&qid=1764853093&sprefix=mario+bros+switch%2Caps%2C161&sr=8-5&ufe=app_do%3Aamzn1.fos.03979ec5-04c0-4e2b-b2cb-0da67477c2a5"
options = webdriver.ChromeOptions()
print(options)
my_webdriver = webdriver.Chrome()
my_webdriver.get(url=URL)
price = my_webdriver.find_element(by=By.CSS_SELECTOR, value="div #corePriceDisplay_desktop_feature_div span .a-price-whole")
price = price.text
product_name = my_webdriver.find_element(by=By.CSS_SELECTOR, value="span#productTitle")
product_name = product_name.text
print(product_name)

from smtplib import SMTP
from dotenv import load_dotenv
import os

load_dotenv()
email_address = os.getenv("EMAIL_ADDRESS")
amazon_password = os.getenv("AMAZON_TRACKER_PASSWORD")
smtp_address = os.getenv("SMTP_ADDRESS")


def send_email(smtp: str, from_email: str, to_email: str, password: str)-> None:
    try:
        with SMTP(host=smtp_address, port=587) as connection:
            connection.starttls()
            connection.login(user=email_address, password=password)
            connection.sendmail(from_addr=email_address, to_addrs=email_address, msg=f"Subject:Amazon Price Alert!\n\nThe product: {product_name} which have you been lookin forward is: {price}, just take a look: {URL}")
            print("The email was sent successfully")
    except BaseException as e:
        print(f"Something happend: {e}")

if float(price) < 800:
    send_email(smtp_address, email_address, email_address, amazon_password)
else: 
    print(f"The price of the product: {product_name} is still high: {price}")