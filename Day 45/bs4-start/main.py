from bs4 import BeautifulSoup

with open("./website.html", "rt") as file:
    contents = file.read()
print(file)
print(f"contents: {contents}")

bs = BeautifulSoup(contents, "html.parser")
print(bs.prettify())
print(f"title: {bs.title}")
print(f"title content: {bs.title.string}")
print(f"title tag: {bs.title.name}")

print(f"first anchor tag: {bs.a}")
print()
