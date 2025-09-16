import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)

response = requests.get("http://api.open-notify.org/iss-now.json")
data = response.json()
print(data)
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
iss_position = (latitude, longitude)
print(iss_position)

response = requests.get("http://api.open-notify.org/is-now.json")
response.raise_for_status()
