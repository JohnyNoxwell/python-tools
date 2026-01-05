def count_vowels(text):
    count = 0
    vowels = "aeiou"
    for symbol in text:
        if symbol.lower() in vowels:
            count += 1

    return count


vowels_in_text = count_vowels("some random text")
print(vowels_in_text)
# This script defines a function to count the number of vowels in a given text string
# and demonstrates its usage by counting vowels in the string "some random text".
# The function is case-insensitive and considers 'a', 'e', 'i', 'o', 'u' as vowels.
