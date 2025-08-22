from bs4 import BeautifulSoup

# import lxml

with open("webscrab1.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# # soup = BeautifulSoup(contents, "lxml")
# print(soup.title)
# print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))
