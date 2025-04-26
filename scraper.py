import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL
BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

# Lists to store data
titles = []
prices = []
ratings = []

# Loop through first 5 pages (can be increased)
for page in range(1, 6):
    print(f"Scraping page {page}...")
    url = BASE_URL.format(page)
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to load page {page}")
        continue

    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        rating_class = book.p.get("class")[1]  # e.g., "Three"
        rating = ["Zero", "One", "Two", "Three", "Four", "Five"].index(rating_class)

        titles.append(title)
        prices.append(price)
        ratings.append(rating)

# Save to CSV
data = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Rating (0-5)": ratings
})
data.to_csv("books.csv", index=False)
print(" Scraping complete! Data saved to 'books.csv'")
