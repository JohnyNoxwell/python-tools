def count_wordsaa(words):
    counted = {}
    for word in words:
        counted[word] = counted.get(word, 0) + 1
    return counted


b = count_wordsaa(["a", "b", "a", "c", "b", "a"])
print(b)
