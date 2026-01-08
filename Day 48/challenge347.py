# Challenge. 347

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", False)

driver = webdriver.Chrome(chrome_options)

driver.get("https://www.python.org/")
ul = driver.find_element(By.CSS_SELECTOR, ".medium-widget.event-widget.last > div > h2.widget-title + p + ul").text
ul = ul.split("\n")
print(ul)
time = [ul[i] for i in range(0, len(ul), 2)]
events = [ul[i] for i in range(1, len(ul), 2)]
print(time)
print(events)
u_e = {}
i = 0
for time,event in zip(time, events):
    u_e[i] = {"time": time, "name": event}
    i += 1
print(u_e)

events_date = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last ul li time")
events_description = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last ul li a")

upcoming_events = {}
for i in range(len(events_date)):
    upcoming_events[i] = {
        "time": events_date[i].text,
        "name": events_description[i].text,
    }
print(upcoming_events)

# Comprehension
upcoming_events = {i: {"time": t.text, "name": d.text} for i, (t, d) in enumerate(zip(events_date, events_description))}
print(upcoming_events)
