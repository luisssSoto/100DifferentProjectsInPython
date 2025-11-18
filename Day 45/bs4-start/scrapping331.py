from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

anchors = soup.select(selector="span.titleline >a")
print(anchors)
print(len(anchors))
anchor_text = []
anchor_urls = []
for anchor in anchors:
    anchor_text.append(anchor.getText())
    anchor_urls.append(anchor.get("href"))
print(anchor_text)
print(anchor_urls)

anchor_votes = [int(item.getText().split()[0]) for item in soup.find_all(name="span", class_="score")]
print(anchor_votes)
max_votes = anchor_votes[0]
max_index = 0
for i in range(1, len(anchor_votes)):
    if anchor_votes[i] > max_votes:
        max_votes = anchor_votes[i]
        max_index = i
print(max_index)
article_most_voted = f"article: {anchor_text[max_index]}\nurl: {anchor_urls[max_index]}\nscore: {str(anchor_votes[max_index])}"
print(article_most_voted)
