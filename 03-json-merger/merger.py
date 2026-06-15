import json
import argparse

def merge_files(files: list) -> dict:
    result = {}
    for filename in files:
        with open(filename, "r") as f:
            data = json.load(f)
            result.update(data)
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge json files")
    parser.add_argument("files", nargs="+", help="Files to merge")
    args = parser.parse_args()

    merge = merge_files(args.files)
    print(json.dumps(merge, indent=2, ensure_ascii=False))