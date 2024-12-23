print("LA:8")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("Lester's book", "Mitch")
print(f"Title: {book.title}, Author: {book.author}")

del book.author

try:
    print(book.author)
except AttributeError as e:
    print(e)

book1 = Book("Marwin The Explorer", "Mitchel")
print(f"Title: {book1.title}, Author: {book1.author}")
