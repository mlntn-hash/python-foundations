import csv

columbs = {}

with open("data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for key, value in row.items():
            if key not in columbs:
                columbs[key] = []
            columbs[key].append(value)


def analyze(values):
    numbers = []
    missing = 0
    for value in values:
        if value == "":
            missing += 1
        else:
            try:
                numbers.append(float(value))
            except ValueError:
                pass

    if numbers and len(numbers) == len(values) - missing:
        col_type = "number"
    else:
        col_type = "text"

    result = {
        "type": col_type,
        "missing": missing,
    }

    if col_type == "number":
        result["min"] = min(numbers)
        result["max"] = max(numbers)
        result["mean"] = sum(numbers) / len(numbers)

    return result

for col_name, values in columbs.items():
    stats = analyze(values)
    print(f"\n--- {col_name} ---")
    for key, value in stats.items():
        print(f"\t{key}: {value}")


