from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver import ActionChains
import time, os
from dotenv import load_dotenv

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/")
        email_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
        email_input.send_keys(username)
        pass_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="pass"]')
        pass_input.send_keys(password)
        login_btn = self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Log In"]')
        login_btn.click()
        self.driver.implicitly_wait(8)
        not_now_btn = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Not now')]")
        not_now_btn.click()

    def find_followers(self, account):
        search_svg = self.driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Search"]')
        search_svg.click()
        search_input = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Search input"]')
        search_input.send_keys(account)
        time.sleep(3)
        account_anchor = self.driver.find_element(By.CSS_SELECTOR, f'div[class^="html-div"] > a[href="/f{account}/"]')
        account_anchor.click()
        self.driver.implicitly_wait(3)


    def follow(self, account):
        followers_anchor = self.driver.find_element(By.CSS_SELECTOR, f'a[href="/{account}/followers/"]')
        followers_anchor.click()
        self.driver.implicitly_wait(3)
        follow_btns = self.driver.find_elements(By.CSS_SELECTOR, 'button[class^=" _aswp _aswr _aswu"]')
        iframe = self.driver.find_element(By.CSS_SELECTOR, 'div[class^="x7r02ix"]')
        scroll_origin = ScrollOrigin.from_element(iframe)
        while True:
            count = 0
            y = 100
            for i in range(len(follow_btns)):
                follow_btns[i].click()
                if count == 5:
                    count = 0
                    ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, y).perform()
                    y += 100
                count += 1
            break

load_dotenv()
user = os.getenv("INSTA_USERNAME")
passw = os.getenv("PASSWORD")
insta_follower = InstaFollower()
insta_follower.login(user, passw)
sim_account = os.getenv("SIMILAR-ACCOUNT")
insta_follower.find_followers(sim_account)
insta_follower.follow(sim_account)
