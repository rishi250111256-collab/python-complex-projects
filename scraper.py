import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve data")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    quotes_data = []

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        quotes_data.append([text, author])

    save_to_csv(quotes_data)
    print("Scraping completed. Data saved to quotes.csv")

def save_to_csv(data):
    with open("quotes.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author"])
        writer.writerows(data)

if __name__ == "__main__":
    scrape_quotes()
