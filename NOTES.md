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
