def top_lengths(text):
    words = {}
    cleaned_words = text.split()
    for word in cleaned_words:
        cleaned_word = word.strip(",.!?;:\"'()[]{}").lower()
        if not cleaned_word:
            continue
        words[cleaned_word] = len(cleaned_word)
    return words


c = top_lengths("Python is really powerful")
print(c)
