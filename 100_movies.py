import requests
from bs4 import BeautifulSoup

# API endpoint (contains the article HTML with all titles)
URL = "https://www.empireonline.com/wp-json/wp/v2/posts/?slug=best-movies-2"

response = requests.get(URL)
data = response.json()

# Extract the rendered HTML content
content_html = data[0]["content"]["rendered"]

soup = BeautifulSoup(content_html, "html.parser")

# Get only strong tags (they contain the movie titles)
raw_movies = [tag.get_text() for tag in soup.find_all("strong")]

# Clean out unwanted lines
all_movies = [
    movie
    for movie in raw_movies
    if not any(bad in movie for bad in ["READ MORE", "Starring", "Director"])
]

# Print all movies in order
for movie in all_movies:
    print(movie)
