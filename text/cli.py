import argparse
import requests
from core import normalize, word_frequency, longest_word


def get_text(source: str) -> str:
    if source.startswith(("http://", "https://")):
        r = requests.get(source, timeout=10)
        r.raise_for_status()
        return r.text
    else:
        with open(source, "r", encoding="utf-8") as f:
            return f.read()


def main():
    parser = argparse.ArgumentParser(description="Text analytics")
    parser.add_argument("source", help="File path or URL")
    parser.add_argument("--top", type=int, default=10, help="Top N words")

    args = parser.parse_args()

    text = get_text(args.source)
    words = normalize(text)
    freq = word_frequency(words)

    top = sorted(freq.items(), key=lambda x: x[1], reverse=True)[: args.top]

    print("\nTop words:")
    for word, count in top:
        print(f"{word}: {count}")

    print("\nLongest word:", longest_word(words))


if __name__ == "__main__":
    main()
