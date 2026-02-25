import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://pokeapi.co/"

# Fetch the webpage
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)

# 1. Extract page title
title = soup.title.text
print("Page Title:", title)

# 2. Extract all links
print("\nLinks found on the page:")
for link in soup.find_all("a"):
    print(link.get("href"))
