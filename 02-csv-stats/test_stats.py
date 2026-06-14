from stats import analyze

def test_analyze():
    result = analyze(["25", "30", "28"])
    assert result["type"] == "number"
    assert result["missing"] == 0
    assert result["min"] == 25.0
    assert result["max"] == 30.0

def test_text_column():
    result = analyze(["Anna", "Oleg", "Maria"])
    assert result["type"] == "text"
    assert result["missing"] == 0

def test_missing_values():
    result = analyze(["25", "", "28"])
    assert result["missing"] == 1

def test_mean():
    result = analyze(["10", "20", "30"])
    assert result["mean"] == 20.0