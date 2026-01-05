def word_lenghts(text):
    words = text.split(" ")
    counts = {}
    for word in words:
        if word not in counts:

            cleaned_word = word.strip(",.!?;:\"'()[]{}").lower()
            if len(cleaned_word) == 0:
                continue
            counts[cleaned_word] = len(cleaned_word)
    return counts


counter = word_lenghts("I love programming! ! !! in Python programming")
print(counter)
