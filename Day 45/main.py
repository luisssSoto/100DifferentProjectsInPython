from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
h3 = soup.select(selector="h3.title")
movies = [movie.getText() for movie in h3]
print(movies)
movies = movies[::-1]
print(movies)
movies[58] = "E.T. The Extra Terrestrial"

try:
    with open(file="100 movies.txt", mode="w") as file:
        text = "\n".join(movies)
        file.write(text)
        print("Successfully wrote 100 movie text")
except BaseException as e:
    print("File not found.")
    print(f"error: {e}")




