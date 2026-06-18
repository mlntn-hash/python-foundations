import requests
import csv
from bs4 import BeautifulSoup
import time

URLS = [
    "https://news.ycombinator.com/news",
    "https://news.ycombinator.com/news?p=2",
    "https://news.ycombinator.com/news?p=3",
    "https://news.ycombinator.com/news?p=4",
    "https://news.ycombinator.com/news?p=5",
]

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
    start = time.time()

    all_titles = []
    for url in URLS:
        all_titles.extend(scrape(url, 10))

    elapsed = time.time() - start

    save_to_csv(all_titles, f"articles_sync.csv")
    print(f"[SYNC] Зібрано {len(all_titles)} заголовків за {elapsed:.2f} s")