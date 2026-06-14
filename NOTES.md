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
