from dotenv import load_dotenv
import pprint

date = input("Which year do you want to travel (YYYY-MM-DD): ")
print(date)
year = date[:4]

header = {"User-Agent":
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
              "AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/142.0.0.0 Safari/537.36"
          }
from bs4 import BeautifulSoup
import requests
URL = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(url=URL, headers=header)
soup = BeautifulSoup(response.text, "html.parser")
h3 = soup.select(selector="li > #title-of-a-story")
song_titles = [title.getText().strip() for title in h3]
print(song_titles)
print(len(song_titles))


# Authentication
import spotipy
import os
import json

load_dotenv()

spotipy_client_id = os.getenv("SPOTIPY_CLIENT_ID")
spotipy_client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
spotipy_uri = os.getenv("SPOTIPY_URI")

def authentication(id, secret, uri):
    cache_file_path = ".cache"
    sp = spotipy.oauth2.SpotifyOAuth(client_id=id, client_secret=secret, redirect_uri=uri, scope='playlist-modify-private')
    if not os.path.exists(cache_file_path):
        try:
            sp.get_access_token()
        except json.JSONDecodeError as e:
            print(f"Error reading cache file: {e}")
    with open(cache_file_path, 'r') as file:
        try:
            token_data = json.load(file)
            access_token = token_data['access_token']
            print(f"Step 2")
        except json.JSONDecodeError as e:
            print(f"Error reading cache file: {e}")
        try:
            my_user = spotipy.client.Spotify(auth=access_token)
            my_user.search(f"track:Golden year:{year}")
        except spotipy.client.SpotifyException as e:
            print(f"Error getting token: {e}")
            try:
                sp.get_access_token()
                with open (cache_file_path, "r") as file:
                    token_data = json.load(file)
                    access_token = token_data['access_token']
                    print(f"Step 3")
            except json.JSONDecodeError as e:
                print(f"Error reading cache file: {e}")
    return access_token

print("spotify token")
spotipy_token = authentication(spotipy_client_id, spotipy_client_secret, spotipy_uri)
print(spotipy_token)

def searching_songs(array, sp, query, limit, offset, type):
    try:
        all_songs = sp.search(query, limit, offset, type)
        uri = all_songs["tracks"]["items"][0]["uri"]
        array.append(uri)
    except IndexError as e:
        print(f"We couldn't find any song with the next query: {query}")
        print(e)
#
def adding_uri_songs(titles, user):
    array = []
    for title in titles:
        query = f"track:{title} year:{year}"
        searching_songs(array, user, query, 1, 1, "track")
    return array

my_user = spotipy.client.Spotify(auth=spotipy_token)
uri_list = adding_uri_songs(song_titles, my_user)
print(f"Step 4")
# print(f"my uri list: {uri_list}")
# print(len(uri_list))

# Create a playlist
print(my_user)
print(f"my user: {my_user.current_user()}")
user_id = my_user.current_user()["id"]
print(f"my user id: {user_id}")

playlist = my_user.user_playlist_create(user_id, name=f"{date} Billboard 100", public=False, )
print(playlist)

# playlist
playlist_id = playlist["id"]
print(playlist_id)
playlist_uri = playlist["uri"]
print(playlist_uri)

my_user = spotipy.client.Spotify(auth=spotipy_token)
print(f"uri list: {uri_list}")

try:
    my_user.playlist_add_items(playlist_uri, uri_list)
except spotipy.client.SpotifyException as e:
    print("Sorry we couldn't add the tracks to the playlist")
    print(e)
