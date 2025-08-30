def count_words(text):
    words = text.split()
    return len(words)

def count_characters(book_text):
    text = book_text.lower()

    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count
