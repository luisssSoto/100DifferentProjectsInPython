from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
import os, time
from dotenv import load_dotenv

class InternetSpeedTwitterBot:
    def __init__(self, down, up):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.down = down
        self.up = up
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.CSS_SELECTOR, 'a[href="#" ] > span[class="start-text"]')
        go_button.click()
        time.sleep(40)
        windows = self.driver.window_handles
        print(windows)
        download_speed_span = self.driver.find_element(By.CSS_SELECTOR, 'span[class^="result-data-large number result-data-value download"]')
        upload_speed_span = self.driver.find_element(By.CSS_SELECTOR, 'span[class^="result-data-large number result-data-value upload"]')
        down_speed = download_speed_span.text
        up_speed = upload_speed_span.text
        return [down_speed, up_speed]

    def tweet_at_provider(self, email, password, curr_down, curr_up):
        self.driver.get("https://x.com/")
        sign_in_btn = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
        sign_in_btn.click()
        windows = self.driver.window_handles
        pop_win = windows[1]
        self.driver.switch_to.window(pop_win)
        email_input = self.driver.find_element(By.CSS_SELECTOR, 'input[class^="r-30o5oe"]')
        email_input.send_keys(email)
        next_btn = self.driver.find_element(By.CSS_SELECTOR, 'div[class^="css-175oi2r"] > button[class^="css-176oi2r"')
        next_btn.click()
        windows = self.driver.window_handles
        pop_win = windows[1]
        self.driver.switch_to.window(pop_win)
        password_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        password_input.send_keys(password)
        login_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[class^="css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19"]')
        login_btn.click()
        self.driver.implicitly_wait(3)

        post_area = self.driver.find_element(By.CSS_SELECTOR, 'div[class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')
        post_area.click()
        post_area.send_keys(f"Hey Internet Provider: Why my internet speed is: {curr_down}down/{curr_up}up when I pay for: {self.down}down/{self.up}up?")
        post_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[class^="css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-1cw"]')
        post_btn.click()

load_dotenv()
download_speed = os.getenv("PROMISED_DOWN")
upload_speed = os.getenv("PROMISED_UP")
internetSpeedTwitterBot = InternetSpeedTwitterBot(download_speed, upload_speed)
internet_speed = internetSpeedTwitterBot.get_internet_speed()
print(internet_speed)
my_email = os.getenv("TWITTER_EMAIL")
my_pass = os.getenv("TWITTER_PASSWORD")
internetSpeedTwitterBot.tweet_at_provider(my_email, my_pass, internet_speed[0], internet_speed[1])


# Notes:
# twitter_user_name: SotoLuisAlex