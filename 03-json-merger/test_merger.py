import json
import pytest
from merger import merge_files

def test_past_files():
    result = merge_files(["file1.json", "file2.json", "file3.json"])
    assert result["age"] == 30
    assert result["city"] == "Lviv"

def test_one_file():
    result = merge_files(["file1.json"])
    assert result == {"name": "Anna", "age": 25}

def test_empty_file():
    with open("empty.json", "w") as f:
        json.dump([], f)
    result = merge_files(["file1.json", "empty.json"])
    assert result == {"name": "Anna", "age": 25}

def test_missing_file():
    with pytest.raises(FileNotFoundError):
        merge_files(["file1.json", "file8.json"])