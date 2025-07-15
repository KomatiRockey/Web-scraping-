
import requests
from bs4 import BeautifulSoup
import csv

URL = "http://books.toscrape.com/"
response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    with open("books.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Rating"])

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.strip()
            rating = book.p["class"][1]
            writer.writerow([title, price, rating])

    print("Data scraped and saved to books.csv.")
else:
    print("Failed to retrieve the webpage.")
