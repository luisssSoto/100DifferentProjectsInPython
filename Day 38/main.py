from dotenv import load_dotenv
import os
import requests
import datetime

load_dotenv()
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("APP_KEY")

nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

nutritionix_params = {
    "query": input("Tell me which exercises you did: ")
}

response = requests.post(nutritionix_exercise_endpoint, json=nutritionix_params, headers=headers)
data = response.json()

my_exercise = data["exercises"][0]["name"].title()
my_duration = data["exercises"][0]["duration_min"]
my_calories = data["exercises"][0]["nf_calories"]

today = datetime.datetime.now()
my_time = today.strftime("%H:%M:%S")
my_date = today.strftime("%d/%m/%Y")

TOKEN = os.environ.get("TOKEN")
bearer_token = {
    "Authorization": f"Bearer {TOKEN}"
}

workouts = {
    "workout": {
        "date": my_date,
        "time": my_time,
        "exercise": my_exercise,
        "duration": my_duration,
        "calories": my_calories,
    }
}

sheet_endpoint = "https://api.sheety.co/c12db56504563295f7629b0fbf1c32d5/myWorkouts/workouts"
response = requests.post(sheet_endpoint, json=workouts, headers=bearer_token)