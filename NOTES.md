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

## L07 — mini-orm

**What I built:** A minimal, dataclass-based ORM layer over SQLite — a `User` class with `save()`, `get()`, and `delete()` methods, using only the standard library (`dataclasses`, `sqlite3`). No external dependencies.

**What I learned:**
- @dataclass — auto-generating __init__ from typed class fields
- sqlite3 basics: connect(), execute() with parameterized queries (?), commit(), close(), fetchone(), cursor.lastrowid
- @staticmethod vs @classmethod — when a method needs `cls` to construct new instances (get()) vs when it doesn't need any instance/class state (_connect())
- SQLite transactions: changes aren't persisted to disk until conn.commit() is called — closing a connection without committing silently discards the change
- monkeypatch (pytest fixture) — temporarily replacing a module-level variable (DB_NAME) for the duration of a test, so tests don't touch the real database file
- Writing a fixture with `yield` to set up test state (temp DB + table) before each test runs

**Where I got stuck (a lot, this time):**
- multiple rounds of indentation mistakes — methods and even whole test functions accidentally defined outside/nested incorrectly, making them invisible to the class or to pytest's test collection ("collected 0 items")
- trailing comma in a multi-line CREATE TABLE string caused a SQL syntax error
- typo: INSENT instead of INSERT
- mismatched table name (user vs users) between CREATE TABLE and the other queries
- UPDATE query had 4 placeholders but only 3 parameters supplied — twice, in two separate fixes
- the trickiest bug: conn.commit() and conn.close() were nested inside the else branch of save(), so new INSERT calls were silently never persisted to disk — found by adding a debug print() to compare the row id vs the query result
- a method name mismatch (create_table vs _create_table) between orm.py and the test fixture

**Time spent:** ~3.5 hours

## L08 — git-trainer

**What I built:** Practiced core Git workflows — branch, merge, rebase, cherry-pick, revert — in an isolated sandbox repo (`git-trainer`, kept separate from this monorepo to avoid nested-repo issues). Intentionally created and resolved both a merge conflict and a cherry-pick conflict.

**What I learned:**
- branch + merge: creating a branch, making divergent changes on the same line in two branches, and resolving the resulting conflict markers (<<<<<<< / ======= / >>>>>>>) by hand
- rebase vs merge: rebase rewrites history into a single linear sequence (no merge commit), while merge preserves both branches' history and adds an explicit merge commit
- cherry-pick: applying one specific commit from a branch without bringing in the rest of that branch's history — and that this can still conflict if the target branch is missing context lines the commit's diff depends on
- revert: creates a brand-new commit that undoes a previous commit's changes, rather than erasing it from history — safer for shared/pushed commits than rewriting history
- git log --oneline (and the graph view in VS Code) for visualizing how branch/merge/rebase/cherry-pick/revert actually shape commit history

**Where I got stuck:**
- git checkout main failed because the sandbox repo's default branch was still named master, not main
- the cherry-pick conflict could only be resolved by keeping a line from the "skipped" commit as context — learned that cherry-pick isn't always a perfectly isolated transplant
- revert removed more than expected (back to 3 lines instead of just undoing the last 2 added lines), because the diff being reverted was larger than anticipated due to how the conflict had been resolved earlier

**Time spent:** ~30 minutes

## L09 — docker-hello

**What I built:** Packaged the Task 5 web scraper into a Docker image. `docker run` builds and runs the container, executing the scraper exactly as it would run locally — without needing Python or any libraries installed on the host.

**What I learned:**
- Dockerfile basics: FROM (base image), WORKDIR, COPY, RUN, CMD
- Why dependencies (requirements.txt) are copied and installed in a separate, earlier layer than the application code — so Docker can reuse the cached "install" layer when only the code changes, instead of reinstalling everything on every build
- docker build -t <name> . — building an image from a Dockerfile and tagging it with a readable name
- docker run <image> — creating and starting a container from an image
- Containers are isolated from the host filesystem by default — a file created inside a container (like articles.csv) doesn't appear on the host unless explicitly shared
- Volumes/bind mounts (-v host_path:container_path) — mapping a host folder to a folder inside the container so files created inside the container are immediately visible on disk

**Where I got stuck:**
- typo in the Dockerfile: --no-cashe-dir instead of --no-cache-dir caused pip to fail with "no such option"
- needed to understand why splitting COPY requirements.txt / RUN pip install from COPY scraper.py matters for build caching, instead of just doing one COPY for everything

**Time spent:** ~30 minutes