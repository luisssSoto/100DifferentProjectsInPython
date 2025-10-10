import requests
from dotenv import load_dotenv
import os

# 1. post
pixela_endpoint = "https://pixe.la/v1/users"

load_dotenv()
token = os.getenv("TOKEN")
user = os.getenv("USER")
pixela_params = {
    "token": token,
    "username": user,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=pixela_params)
print(response.text)

# 2. post

graph_endpoint = f"{pixela_endpoint}/{user}/graphs"
GRAPH_ID = "graph1"
graph_params = {
    "id": GRAPH_ID,
    "name": "coding_graph",
    "unit": "day",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": token
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)

post_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# 3. post

import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)

post_params = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "1"
}

response = requests.post(headers=headers, url=post_endpoint, json=post_params)
print(response.text)

# 4. put
put_endpoint = f"{post_endpoint}/{today.strftime("%Y%m%d")}"
put_params = {
    "quantity": "4"
}

response = requests.put(headers=headers, url=put_endpoint, json=put_params)
print(response.text)

# 5. delete
response = requests.delete(url=put_endpoint, json=put_params, headers=headers)
print(response.text)