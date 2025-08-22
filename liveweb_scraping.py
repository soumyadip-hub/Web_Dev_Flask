# from bs4 import BeautifulSoup

# import requests

# response = requests.get("https://www.cemkolaghat.in/")

# print(response.text)

from bs4 import BeautifulSoup
import requests

url = "https://www.cemkolaghat.in/"
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Example 1: Get the page title
print("Page Title:", soup.title.string)

# Example 2: Get all links
for link in soup.find_all("a", href=True):
    print("Link text:", link.text.strip(), "URL:", link["href"])

# Example 3: Get all visible text
for paragraph in soup.find_all("p"):
    print("Paragraph:", paragraph.get_text(strip=True))
