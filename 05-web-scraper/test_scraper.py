import pytest
import csv
from scraper import save_to_csv, scrape

def test_scraper():
    titles = scrape("https://news.ycombinator.com", 5)
    assert isinstance(titles, list)
    assert len(titles) == 5

def test_scraper_zero():
    titles = scrape("https://news.ycombinator.com", 0)
    assert titles == []

def test_save(tmp_path):
    titles = ["title1", "title2", "title3"]
    filespath = tmp_path / "test.csv"
    save_to_csv(titles, str(filespath))

    with open(filespath, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)


    assert rows[0] == ["titles"]
    assert rows[1] == ["title1"]
    assert len(rows) == 4


