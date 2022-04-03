from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)

response = requests.get("https://news.ycombinator.com/")
print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.find(name="a", class_="titlelink"))
articles = soup.find_all(name="a", class_="titlelink")
article_title = []
article_links = []
article_votes = []
for article_tag in articles:
    article_title.append(article_tag.getText())
    article_links.append(article_tag.get("href"))

article_upvotes = soup.find_all(name="span", class_="score")

for votes in article_upvotes:
    article_votes.append(int(votes.getText().split()[0]))
print(article_title)
print(article_votes)
print(article_links)

print(article_votes.index(max(article_votes)))
max_index = article_votes.index(max(article_votes))
print(article_title[max_index])
print(article_links[max_index])
