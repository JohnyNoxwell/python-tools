def word_frequency(text):
    counts = {}
    words = text.split(" ")

    for word in words:
        clean_word = word.strip(",.!?;:\"'()[]{}").lower()

        if not clean_word:
            continue

        if clean_word in counts:
            counts[clean_word] += 1
        else:
            counts[clean_word] = 1
        
    return counts


test = word_frequency("test!! test !!! stest another word here another")
print(test)
