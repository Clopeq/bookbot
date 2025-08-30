
import sys
from stats import sort_dictionary
from stats import count_words
from stats import count_characters

def get_book_text(book):
    book_contents = None

    with open(book) as f:
        book_contents = f.read()

    return book_contents


def main():
    
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")

    book_text = get_book_text(file)

    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    
    char_count = count_characters(book_text)

    print("--------- Character Count -------")
    
    dict_list_char_count = []
    for key in char_count:
        if key.isalpha():
            dict_list_char_count.append({"char": key, "num": char_count[key]})
    dict_list_char_count = sort_dictionary(dict_list_char_count)

    for item in dict_list_char_count:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
