import string


PUNCT = string.punctuation


def normalize(text: str) -> list[str]:
    text = text.lower()
    for ch in PUNCT:
        text = text.replace(ch, "")
    return text.split()


def word_frequency(words: list[str]) -> dict[str, int]:
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts


def word_lengths(words: list[str]) -> dict[str, int]:
    return {w: len(w) for w in set(words)}


def longest_word(words: list[str]) -> str:
    if not words:
        return ""
    return max(words, key=len)


def count_vowels(text: str) -> int:
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch in vowels)
