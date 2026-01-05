def normalize_text(text):
    text = text.lower().strip().replace(".", "").replace(",", "")
    words = text.split()
    return words


words_list = normalize_text("  Hello, World. Python  ")
print(words_list)
