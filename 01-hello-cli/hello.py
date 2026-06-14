import argparse

def green(name):
    return {
        "en": f"Hello, {name}",
        "de": f"Hallo, {name}",
        "uk": f"Привіт, {name}",
    }

if __name__ == "__main__":
 parser = argparse.ArgumentParser()
 parser.add_argument("name")
 args = parser.parse_args()
 for lang, message in green(args.name).items():
    print(f"[{lang}] {message}")