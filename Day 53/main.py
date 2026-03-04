from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import requests, os, time, subprocess

# 1. Get the data from Zillow
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

response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

url_property = soup.select(selector='a[class="StyledPropertyCardDataArea-anchor"]')
url_property_list = [link.get('href') for link in url_property]
print(url_property_list)

address_property = soup.select(selector='a[class="StyledPropertyCardDataArea-anchor"] > address')
address_property_list = [(address.getText().strip()).replace("|", "") for address in address_property]
print(address_property_list)

price_property = soup.select(selector='span[class="PropertyCardWrapper__StyledPriceLine"]')
price_property_list = [price.getText()[:6] for price in price_property]
print(price_property_list)

# 2. Use Selenium to fill the form
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
user_data_dir = r"C:\selenium-profile"

# This wait until chrome.exe is executed then Selenium can be executed
subprocess.Popen([
    chrome_path,
    "--remote-debugging-port=9222",
    f"--user-data-dir={user_data_dir}"
])

time.sleep(3)
options = Options()
options.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=options)

load_dotenv()
google_form_user = os.getenv("GOOGLE_FORM_USER")
print(google_form_user)
driver.get(google_form_user)

for i in range(len(address_property_list)):
    questions = driver.find_elements(By.CSS_SELECTOR, 'input[class="whsOnd zHQkBf"]')
    questions[0].click()
    questions[0].send_keys(address_property_list[i])
    questions[1].send_keys(price_property_list[i])
    questions[2].send_keys(url_property_list[i])
    submit_btn = driver.find_element(By.XPATH, "//span[contains(text(), 'Enviar')]")
    submit_btn.click()
    time.sleep(1)
    come_back_btn = driver.find_element(By.XPATH, "//a[contains(text(), 'Enviar otra respuesta')]")
    come_back_btn.click()
    print(f"question: #{i + 1} submitted")

google_form_admin = os.getenv("GOOGLE_FORM_ADMIN")
driver.get(google_form_admin)
time.sleep(3)
create_sheet_btn = driver.find_element(By.XPATH, '//span[contains(text(), "Vínculo a Hojas de cálculo")]')
create_sheet_btn.click()
confirm_btns = driver.find_elements(By.XPATH, '//span[contains(text(), "Crear")]')
confirm_btn = confirm_btns[-1]
confirm_btn.click()