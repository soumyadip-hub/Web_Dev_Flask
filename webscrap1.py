from bs4 import BeautifulSoup

# import lxml

with open("webscrab1.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# # soup = BeautifulSoup(contents, "lxml")
print(soup.title)
print(soup.prettify())
