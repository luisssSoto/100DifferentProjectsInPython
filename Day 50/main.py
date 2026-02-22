from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
my_driver = webdriver.Chrome(options=chrome_options)

my_driver.get("https://tinder.com/")
my_driver.implicitly_wait(3)
login_btn = my_driver.find_element(By.CSS_SELECTOR, 'a[class^="c1p6lbu0"]')
login_btn.click()
my_driver.implicitly_wait(3)
log_phone_btn = my_driver.find_element(By.CSS_SELECTOR, 'div[class^="Mend(a)"]')
log_phone_btn.click()
windows = my_driver.window_handles
print(len(windows))
pop_up_window = windows[-1]
my_driver.switch_to.window(pop_up_window)
phone_num_input = my_driver.find_element(By.CSS_SELECTOR, 'input#phone_number')
phone_num_input.send_keys("333333333")
next_btn = my_driver.find_element(By.CSS_SELECTOR, 'div[class^="Mt(a)"] > button')
next_btn.click()
wait = WebDriverWait(my_driver, 1000)
print(wait)

allow_btn = my_driver.find_element(By.CSS_SELECTOR, 'div[class^="Bgc"] button[class^="c1p6lbu0 W(100%)"')
allow_btn.click()
miss_nots_btn = my_driver.find_element(By.CSS_SELECTOR, 'button[aria-label="I’ll miss out"]')
miss_nots_btn.click()
accept_cookies_btn = my_driver.find_element(By.CSS_SELECTOR, 'div[class^="D(f)--ml"] button[class^="c1p6lbu0 "]:first-of-type')
accept_cookies_btn.click()

for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = my_driver.find_element(By.XPATH, value=
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = my_driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

my_driver.quit()
