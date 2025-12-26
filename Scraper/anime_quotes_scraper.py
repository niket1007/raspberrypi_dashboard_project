import requests
from bs4 import BeautifulSoup
import json

links = set()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for page in range(1, 18):
    print(f"Fetching quote page links from page number {page}")
    response = requests.get(f"https://animemotivation.com/page/{page}/?s=quotes", headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    
    tags_a = soup.find_all("a", class_="plain")
    for tag_a in tags_a:
        links.add(tag_a["href"])

print("Total Links", len(links))

quotes = set()
for link in links:
    print(f"Fetching quotes from {link}")
    if link.startswith("https:") or link.startswith("http:"):
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        blockquotes = soup.find_all("blockquote")
        for blockquote in blockquotes:
            quotes.add(blockquote.text)
quotes_list = []
for quote in quotes:
    quotes_list.append({
        "quote": quote
    })
with open("quotes.json", "w") as file:
    json.dump(quotes_list, file, indent=4)