from stats import get_num_words

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()
    
if __name__ == "__main__":
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(book_text)
    print(f'Found {word_count} total words')