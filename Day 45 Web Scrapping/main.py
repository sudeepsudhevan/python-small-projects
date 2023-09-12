from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.a.getText()
    article_texts.append(text)

    link = article_tag.a.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

highest_value = max(article_upvotes)
index = article_upvotes.index(highest_value)
# print(index)

print(article_texts[index])
print(article_links[index])





# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
#
# # print(soup.a)
# all_anchor_tags = soup.find_all(name="a")
#
#
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href")) for get attribute value
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())
# company_url = soup.select_one(selector="#name")
# # print(company_url)
#
#
# headings = soup.select(selector=".heading")
# print(headings)
