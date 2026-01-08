from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
articles = driver.find_element(By.CSS_SELECTOR, "#articlecount ul li +li > a:first-child").text
print(articles)

# 349. Lesson
# click() method
link = driver.find_element(By.LINK_TEXT, "Content portals")
link.click()

# typing
advertisement = driver.find_element(By.CSS_SELECTOR, "button.frb-icon-btn.frb-close.skin-invert")
advertisement.click()
lupa = driver.find_element(By.CSS_SELECTOR, "a span.vector-icon.mw-ui-icon-search.mw-ui-icon-wikimedia-search")
lupa.click()
search = driver.find_element(By.CSS_SELECTOR, "#searchform input.cdx-text-input__input")
print(search.get_attribute("name"))
wait = WebDriverWait(driver, timeout=2)
wait.until(lambda _: search.is_displayed())
search.send_keys("Python", Keys.ENTER)