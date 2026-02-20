from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import time, calendar, datetime


# 1. Login
def login():
    """Login Gym Website"""
    login_button = my_driver.find_element(By.CSS_SELECTOR, "#login-button")
    login_button.click()

    my_driver.implicitly_wait(3)
    email_button = my_driver.find_element(By.CSS_SELECTOR, "#email-input")
    email_button.clear()
    email_button.send_keys(account_email)
    password_button = my_driver.find_element(By.CSS_SELECTOR, "#password-input")
    password_button.clear()
    password_button.send_keys(account_password)
    submit_button = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#submit-button")))
    submit_button.click()
    time.sleep(3)

def retry(functions, retries, description):
    if description == "login":
        func = functions[0]
        func()
        current_page = my_driver.current_url
        while current_page != gym_url + 'schedule/':
            retries += 1
            print(f"Trying to login. Attempt: {retries}")
            func()
            current_page = my_driver.current_url
    elif description == "book":
        func = functions[1]
        was_booked = func()
        while not was_booked:
            retries += 1
            print(f"Trying to booking. Attempt: {retries}")
            was_booked = func()
        else:
            return was_booked
    elif description == "my_bookings":
        func = functions[2]
        is_in_bookings = func()
        while not is_in_bookings:
            retries += 1
            print(f"Trying to booking. Attempt: {retries}")
            is_in_bookings = func()
        else:
            return is_in_bookings
    return description


# 2. Book a class
def find_day_classes(day, current_day):
    """find the classes depending on the day of the week"""
    weekdays = {
        "mon": calendar.MONDAY,
        "tue": calendar.TUESDAY,
        "wed": calendar.WEDNESDAY,
        "thu": calendar.THURSDAY,
        "fri": calendar.FRIDAY,
        "sat": calendar.SATURDAY,
        "sun": calendar.SUNDAY
    }
    css_selector = f'div[id^="day-group-{day}"] > div'
    classes = my_driver.find_elements(By.CSS_SELECTOR, css_selector)
    if len(classes) == 0:
        if current_day == weekdays[day]:
            css_selector = f'div[id^="day-group-today"] > div'
        else:
            css_selector = f'div[id^="day-group-tomorrow"] > div'
        classes = my_driver.find_elements(By.CSS_SELECTOR, css_selector)
    classes_selector = (classes, css_selector)
    return classes_selector

def book_class(day_classes, hour):
    """book and return the details of the booked class"""
    classes_list = day_classes[0]
    day_group_selector = day_classes[1]
    day_classes_button_selector = day_group_selector + '[id ^= "class-card"] button'
    day_classes_buttons = my_driver.find_elements(By.CSS_SELECTOR, day_classes_button_selector)
    class_time_selector = day_group_selector + ' [id^="class-time"]'
    time_classes = my_driver.find_elements(By.CSS_SELECTOR, class_time_selector)
    booked_class = {}
    was_it_booked = False
    was_it_waited = False
    for i in range (len(time_classes)):
        if time_classes[i].text.endswith(hour):
            booked_button = day_classes_buttons[i]
            booked_button_text = booked_button.text
            booked_class["Text"] = booked_button_text
            if booked_button_text == "Booked":
                was_it_booked = True
            elif booked_button_text == "Waitlisted":
                was_it_waited = True
            else:
                name_before_booked = booked_button.text
                booked_button.click()
                time.sleep(3)
                name_after_booked = booked_button.text
                if name_before_booked == name_after_booked:
                    return False
            chosen_class = classes_list[i]
            chosen_class_details = "Name: " + chosen_class.text
            chosen_class_details = chosen_class_details.split("\n")
            for item in chosen_class_details[:-3]:
                key = ""
                for j in range(len(item)):
                    if item[j] == ":":
                        booked_class[key] = item[j + 2:]
                        break
                    key += item[j]
    booked_class["Booked"] = was_it_booked
    booked_class["Waited"] = was_it_waited
    return booked_class

def check_booked_expected_class(booked, current):
    """check if the booked class matches the expected class"""
    for label in booked.keys():
        if booked[label] != current[label]:
            return False
    return True

def look_booked_data(book_join_class, booked_details):
    """create a dict by looking the booking section to validate if the current data is the same as we expected"""
    booking_selector = '> div > div > div[class^="MyBookings"]'
    if book_join_class == "Book Class" or book_join_class == "Booked":
        booking_selector = '#confirmed-bookings-section ' + booking_selector
    elif book_join_class == "Join Waitlist" or book_join_class == "Waitlisted":
        booking_selector = '#waitlist-section ' + booking_selector
    booked_classes = my_driver.find_elements(By.CSS_SELECTOR, booking_selector)
    current_class = {}
    date = ""
    if len(booked_classes) == 0:
        return False
    for cls in booked_classes:
        booked_cls = cls.text.split("\n")
        date = booked_cls[1][6:-8]
        if len(booked_cls) > 3:
            current_class = {
                "Name": booked_cls[0],
                 "Time": booked_cls[1][-7:],
                 booked_cls[2][:10]: booked_cls[2][12:],
            }
        else:
            current_class = {
                "Name": booked_cls[0][:-11],
                "Time": booked_cls[1][-7:],
                booked_cls[2][:10]: booked_cls[2][12:]
            }
        if current_class == booked_details:
            break
    current_class["Date"] = date
    return current_class

def classes_details():
    """Return the details of the booked and wait classes"""
    booking_selector = '> div > div > div[class^="MyBookings"]'
    try:
        booked_area = WebDriverWait(my_driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#confirmed-bookings-section ' + booking_selector)))
    except TimeoutException:
        booked_area = []
        print("TIME OUT for booked area")
    try:
        wait_area = WebDriverWait(my_driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#waitlist-section ' + booking_selector)))
    except TimeoutException:
        wait_area = []
        print("TIME OUT for wait area")
    booked_details = []
    if len(booked_area) > 0:
        for cls in booked_area:
            booked_cls = cls.text.split("\n")
            cls_details = {
                "Name": booked_cls[0],
                "Date": booked_cls[1][6:-8],
                "Time": booked_cls[1][-7:],
                booked_cls[2][:10]: booked_cls[2][12:],
                booked_cls[3][:8]: booked_cls[3][10:],
            }
            booked_details.append(cls_details)
    wait_details = []
    if len(wait_area) > 0:
        for cls in wait_area:
            booked_cls = cls.text.split("\n")
            cls_details = {
                "Name": booked_cls[0][:-11],
                "Date": booked_cls[1][6:-8],
                "Time": booked_cls[1][-7:],
                booked_cls[2][:10]: booked_cls[2][12:]
            }
            wait_details.append(cls_details)
    return [booked_details, wait_details]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
my_driver = webdriver.Chrome(options=chrome_options)

load_dotenv()
account_email = os.getenv("ACCOUNT_EMAIL")
account_password = os.getenv("ACCOUNT_PASSWORD")
gym_url = os.getenv("GYM_URL")

my_driver.get(gym_url)
retry([login], 0, "login")
schedule_anchor = WebDriverWait(my_driver, 10)
schedule_anchor = schedule_anchor.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#schedule-link")))
assert schedule_anchor.text == "Class Schedule"

my_day = "wed"
today = datetime.datetime.now().weekday()
chosen_classes = find_day_classes(my_day, today)

user_hour = "9:00 AM"
booked_class_details = retry([login, lambda: book_class(chosen_classes, user_hour)], 0, "book")
print(f"booked class details: {booked_class_details}")
booked_link = my_driver.find_element(By.CSS_SELECTOR, "#my-bookings-link")
booked_link.click()
booked_btn_text = booked_class_details.pop("Text")
is_it_booked = booked_class_details.pop("Booked")
is_it_waited = booked_class_details.pop("Waited")

current_class_details = retry([login, lambda: book_class(chosen_classes, user_hour), lambda: look_booked_data(booked_btn_text, booked_class_details)], 0, "my_bookings")
print(f"current class details: {current_class_details}")

if is_it_booked:
    print(f"✓ Already booked: {current_class_details["Name"]} on {current_class_details["Date"]}")
elif is_it_waited:
    print(f"✓ Already on waitlist: {current_class_details["Name"]} on {current_class_details["Date"]}")
else:
    if not check_booked_expected_class(booked_class_details, current_class_details):
        print(f"The booked class doesn't match expected class")
    else:
        print("The booked class matches the expected class")
        if booked_btn_text == "Book Class" or booked_btn_text == "Booked":
            print(f'✓ Booked for: {current_class_details["Name"]} on {current_class_details["Date"]}')
        else:
            print(f'✓ Joined waitlist for: {current_class_details["Name"]} on {current_class_details["Date"]}')

current_booked_classes = classes_details()
count_booked_classes = len(current_booked_classes[0])
count_wait_classes = len(current_booked_classes[1])

print()
print(f' --- BOOKING SUMMARY --- \n'
      f'Classes booked: {count_booked_classes}\n'
      f'Waitlists joined: {count_wait_classes}\n'
      f'Already booked/waitlisted: {count_booked_classes + count_wait_classes}\n'
      f'Total booked classes processed: {count_booked_classes}\n'
      f'Details: {current_booked_classes[0]}\n'
      f'Total wait classes processed: {count_wait_classes}\n'
      f'Details: {current_booked_classes[1]}')
