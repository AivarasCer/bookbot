import sys
from stats import (get_num_words, get_num_chars, chars_dict_to_sorted_list)     

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    char_count = get_num_chars(book_text)
    chars_sorted_list = chars_dict_to_sorted_list(char_count)
    print_report(book_path, word_count, chars_sorted_list)


def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
