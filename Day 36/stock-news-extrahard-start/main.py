import os
from dotenv import load_dotenv
import requests
import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
load_dotenv()
API_KEY = os.getenv("ALPHA_API_KEY")
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY,
}

today = datetime.datetime.today()
today = today.date()
yesterday_days = 1
before_yesterday_days = 2

if today.weekday() == 1:
    before_yesterday_days = 4
elif today.weekday() == 0:
    yesterday_days = 3
    before_yesterday_days = 4
elif today.weekday() == 6:
    yesterday_days = 2
    before_yesterday_days = 3

yesterday = str(today - datetime.timedelta(days=yesterday_days))
before_yesterday = str(today - datetime.timedelta(days=before_yesterday_days))

print(yesterday)
print(before_yesterday)

alpha_endpoint = "https://www.alphavantage.co/query"
request = requests.get(alpha_endpoint, params=params)
request.raise_for_status()
print(request)
data = request.json()
print(data)
yesterday_close = float(data["Time Series (Daily)"][yesterday]["4. close"])
print(yesterday_close)
before_yesterday_close = float(data["Time Series (Daily)"][before_yesterday]["4. close"])
print(before_yesterday_close)

diff_close = round(yesterday_close - before_yesterday_close, 2)
print(diff_close)
high_diff = round((yesterday_close + before_yesterday_close) // 2 * 5 / 100, 2)
print(high_diff)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. month_ago
today_date = datetime.date.today()
month_ago = today_date - datetime.timedelta(days = 29)
print(f"current year: {month_ago}")
print(f"month ago: {today_date}")

news_params = {
    "q": COMPANY_NAME,
    "searchIn": "title",
    "from": month_ago,
    "to": today_date,
    "sortBy": "relevancy",
    "apiKey": os.getenv("NEWS_API_KEY"),
}
news_endpoint = "https://newsapi.org/v2/everything"

def get_news(difference, percentage):
    new_message = f"{STOCK}"
    if difference >= percentage:
        new_message += "🔺5%"
        return new_message
    elif difference <= -percentage:
        new_message += "🔻5%"
        return new_message
    else:
        return False

msg = get_news(diff_close, high_diff)

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

account_sid= os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

def send_news(get_info, new_params):
    if get_info:
        msg = get_info
        response = requests.get(news_endpoint, params=new_params)
        response.raise_for_status()
        news_data = response.json()
        three_most_relevant_news = news_data["articles"][:3]
        for new in three_most_relevant_news:
            msg += f"\nHeadline: {new['title']}\nBrief: {new['description']}\nLink: {new['url']}"
            print(msg)
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_="whatsapp:+14155238886",
                body=msg,
                to=f"whatsapp:{os.getenv('TEL_NUMBER')}"
            )
            msg = get_info
    else:
        return None

send_news(msg, news_params)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

