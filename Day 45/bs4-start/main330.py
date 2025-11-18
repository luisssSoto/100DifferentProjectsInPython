from bs4 import BeautifulSoup

with open("./website.html") as file:
    html = file.read()


soup = BeautifulSoup(html, "html.parser")

all_anchor_tags = soup.find_all("a")
print(all_anchor_tags)
for anchor in all_anchor_tags:
    print(anchor.name)
    print(anchor.string)
    print(anchor.getText())
    print(anchor.get("href"))

heading = soup.find("h1")
print(heading)

h3 = soup.find_all(name="h3", class_="heading")
print(h3)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(selector=".heading")
print(headings)