def longest_word(text):
    words = text.split(" ")
    longest_word = ""
    for word in words:
        cleaned_word = word.strip(",.!?;:\"'()[]{}").lower()
        if len(cleaned_word) > len(longest_word):
            longest_word = cleaned_word

    return longest_word


longest_words = longest_word("I love programming! ! !! in Python")
print(longest_words)
