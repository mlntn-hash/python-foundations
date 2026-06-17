import requests
import csv
from bs4 import BeautifulSoup

def scrape(url: str, count: int = 10) -> list:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all("span", class_="titleline")
    return [t.text for t in titles[:count]]

def save_to_csv(titles: list, filename: str) -> None:
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["titles"])
        for title in titles:
            writer.writerow([title])


if __name__ == "__main__":
    titles = scrape("https://news.ycombinator.com", 10)
    save_to_csv(titles, "articles.csv")
    print(f'Збережено: {len(titles)} заголовкв у articles.csv')




