def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()
    
if __name__ == "__main__":
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text[:500])