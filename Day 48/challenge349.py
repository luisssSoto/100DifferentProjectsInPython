# Challenge 349
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Luis")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Soto")
email = driver.find_element(By.NAME, "email")
email.send_keys("chavoRucomon@gmail.com")
sign_up = driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-lg btn-primary btn-block')]")
sign_up.click()
h1 = driver.find_element(By.XPATH, '//h1[contains(@class,"display-3")]')
assert h1.text == "Success!"
