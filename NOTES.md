## L01 — hello-cli

**What I built:** CLI utility that greets in 3 languages with pytest tests

**What I learned:**
- argparse — reading arguments from the terminal
- if __name__ == "__main__" — protection from import
- pytest — automated tests

**Where I got stuck:**
- forgot f before the string
- for loop was outside if __name__

**Time spent:** ~30 minutes

## L02 — csv-stats

**What I built:** CSV reader that outputs column statistics (type, missing values, min/max/mean) without pandas

**What I learned:**
- csv.DictReader — reading CSV as dictionaries
- open() with "r" mode — file reading modes
- try/except — handling errors when converting strings to numbers
- append() — adding elements to a list
- if __name__ == "__main__" — protection from import
- Building column statistics manually with min(), max(), sum(), len()

**Where I got stuck:**
- used `return` before adding min/max/mean to result
- accidentally imported `numbers` and `result` from standard library (PyCharm auto-import)

**Time spent:** ~1 hours

## L03 — json-merger

**What I built:** CLI utility that merges N JSON files with last-wins conflict resolution

**What I learned:**
- json.load() — reading JSON file into Python dict
- json.dumps() — converting dict to formatted JSON string
- dict.update() — merging dictionaries
- nargs="+" — accepting multiple arguments in argparse
- pytest.raises() — testing that errors are raised correctly
- Edge cases — empty files, missing files, duplicate keys

**Where I got stuck:**
- return was inside the for loop instead of outside

**Time spent:** ~1 hour

## L04 — log-parser

**What I built:** CLI utility that parses nginx access logs, counts top-10 IPs and calculates average response time

**What I learned:**
- re module — regular expressions for pattern matching
- \d+ — one or more digits in regex
- () groups in regex — extracting specific parts with match.group()
- collections.Counter — counting occurrences automatically
- most_common(n) — getting top N elements
- tmp_path in pytest — creating temporary files for tests
- pytest.approx() — comparing float numbers with tolerance

**Where I got stuck:**
- named response_times variable as response_time (without s)
- hardcoded "access.log" filename instead of using filename parameter

**Time spent:** ~1.5 hours

## L05 — web-scraper

**What I built:** CLI utility that scrapes article titles from a website and saves them to CSV using requests + BeautifulSoup

**What I learned:**
- requests.get() — fetching HTML content from a website
- BeautifulSoup — parsing HTML and finding elements
- find() vs find_all() — finding one element vs all matching elements
- CSS class selector — class_="..." to find elements by their class
- list slicing — titles[:count] to take first N elements
- list comprehension — [t.text for t in titles] as a compact loop
- default parameter values — count: int = 10
- csv.writer — saving data to CSV files

**Where I got stuck:**
- tried scraping Google instead of a site with matching HTML structure
- typo: scrape.titles instead of scrape_titles
- typo: "urf-8" instead of "utf-8"

**Time spent:** ~1.5 hours

## L06 — async-fetcher

**What I built:** Rewrote the synchronous web scraper from Task 5 using asyncio + aiohttp, fetching 5 Hacker News pages concurrently instead of one by one. Measured and compared execution time between the sync and async versions on the same set of URLs.

**What I learned:**
- async def / await — defining and running coroutines
- aiohttp.ClientSession — async HTTP client; one session is created once and passed into scrape() as a parameter, reused across all requests instead of opening a new session each time
- asyncio.gather() — running multiple coroutines concurrently and collecting results in the same order tasks were submitted
- asyncio.run() — entry point that creates and starts the event loop
- Event loop — how asyncio switches between coroutines while one is waiting on network I/O, instead of blocking
- The difference between .append() and .extend() when flattening a list of lists
- pytest-asyncio and @pytest.mark.asyncio — testing async functions with pytest
- tmp_path pytest fixture — writing test output to a temporary, auto-cleaned directory

**Where I got stuck:**
- used .append() instead of .extend() when merging results from gather(), so titles ended up as 5 nested lists instead of 50 flat strings
- forgot to call asyncio.run(main()) at the end of the file — script exited with code 0 and no output, because the coroutine was defined but never actually executed
- needed clarification on why session is created once in main() and passed into scrape(), rather than scrape() creating its own session each call

**Results:**
- Sync version (5 pages, sequential): 6.42s
- Async version (5 pages, concurrent): 1.11s
- ~5.8x speedup

**Time spent:** ~1.5 hours
