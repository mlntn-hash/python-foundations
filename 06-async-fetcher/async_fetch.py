import asyncio
import aiohttp
import csv
import time
from bs4 import BeautifulSoup

URLS = [
    "https://news.ycombinator.com/news",
    "https://news.ycombinator.com/news?p=2",
    "https://news.ycombinator.com/news?p=3",
    "https://news.ycombinator.com/news?p=4",
    "https://news.ycombinator.com/news?p=5",
]

async def scrape(session: aiohttp.ClientSession, url: str, count: int = 10) -> list:
    async with session.get(url) as response:
        html = await response.text()
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all("span", class_="titleline")
    return [t.text for t in titles[:count]]

def save_to_csv(titles: list, filename: str) -> None:
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["titles"])
        for title in titles:
            writer.writerow([title])

async def main():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [scrape(session, url) for url in URLS]
        results = await asyncio.gather(*tasks)

    all_titles = []
    for titles in results:
        all_titles.extend(titles)

    elapsed = time.time() - start

    save_to_csv(all_titles, f"articles_async.csv")
    print(f"[ASYNC] Зібрано {len(all_titles)} заголовків за {elapsed:.2f} s")

if __name__ == "__main__":
    asyncio.run(main())