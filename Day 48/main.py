# 345. lesson
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", False)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://Google.com")

# Close the tab
# driver.close()

# Close the entire Browser (all the tabs)
# driver.quit()

# 346. lesson
from selenium.webdriver.common.by import By
driver1 = webdriver.Chrome(options=chrome_options)
driver1.get("https://www.python.org/")

'''By class'''
python_logo = driver1.find_element(By.CLASS_NAME, "python-logo")
python_logo_alt = python_logo.get_attribute("alt")
print(python_logo_alt)

search_bar = driver1.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder"))

submit_button = driver1.find_element(By.ID, "submit")
print(submit_button.size)

documentation_link = driver1.find_element(By.CSS_SELECTOR, '#container > :nth-of-type(3) > ul:nth-of-type(1) [href="/doc/"]')
print(documentation_link.text)

bug_link = driver1.find_element(By.XPATH, "//div[@class='site-base']//li[@class='tier-1 element-3']")
print(bug_link.text)
