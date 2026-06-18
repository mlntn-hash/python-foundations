import pytest
import aiohttp
from pip._internal.commands import uninstall

from async_fetch import scrape, save_to_csv

def test_save_to_csv(tmp_path):
    title = ["Title1", "Title2", "Title3"]
    filepath = tmp_path / "test_output.csv"

    save_to_csv(title, str(filepath))

    content = filepath.read_text()
    assert "Title1" in content
    assert "Title2" in content
    assert "Title3" in content

@pytest.mark.asyncio
async def test_scrape():
    async with aiohttp.ClientSession() as session:
        titles = await scrape(session, "https://news.ycombinator.com/news", count=5)

    assert len(titles) == 5
    assert all(isinstance(title, str) for title in titles)
