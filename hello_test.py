from hello import green

def test_en():
    result = green("Anna")
    assert result["en"] == "Hello, Anna"

def test_de():
    result = green("Tetiana")
    assert result["de"] == "Hallo, Tetiana"

def test_uk():
    result = green("Nazar")
    assert result["uk"] == "Привіт, Nazar"