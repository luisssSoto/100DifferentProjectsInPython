from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
my_driver = webdriver.Chrome(chrome_options)

my_driver.implicitly_wait(5)
my_driver.get("https://ozh.github.io/cookieclicker/")

def click_on_language_div(driver):
    """get rid of the language div"""
    language_button = driver.find_element(By.CSS_SELECTOR, "div#langSelect-EN")
    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda _: language_button.is_displayed())
    language_button.click()

def click_on_cookie(driver):
    """click on the cookie button"""
    cookie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")
    cookie.click()

def looking_for_new_upgrades(driver):
    """look for new upgrades to buy"""
    products = driver.find_elements(By.CSS_SELECTOR, "#products .product")
    for i in range(len(products) -1, -1, -1):
        is_it_available = products[i].get_attribute("class") == "product unlocked enabled"
        if is_it_available:
            products[i].click()

import time

click_on_language_div(my_driver)
start_time = time.time()
end_time = start_time + 300
start_seconds = None

while start_time < end_time:
    if not start_seconds:
        start_seconds = time.time()
    current_seconds = time.time()
    if current_seconds >= start_seconds + 10:
        looking_for_new_upgrades(my_driver)
        start_seconds = None
    click_on_cookie(my_driver)
    start_time = time.time()

cookies_data = my_driver.find_element(By.CSS_SELECTOR, "#sectionLeft #cookies").text
cookies_data = cookies_data.split(" ")
cookies_per_second = cookies_data[-1]
print(f"cookies/second: {cookies_per_second}")

my_driver.quit()