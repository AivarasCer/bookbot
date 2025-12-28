def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()
    
def count_words(text):
    words = text.split()
    return len(words)
    
if __name__ == "__main__":
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    print(f'Found {word_count} total words')