# Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"{self.title} by {self.author} ({status})"


# Library class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Added: {book}")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed: {book}")
                return
        print("Book not found.")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Found: {book}")
                return book
        print("Book not found.")
        return None

    def borrow_book(self, title):
        book = self.search_book(title)
        if book and not book.is_borrowed:
            book.is_borrowed = True
            print(f"You borrowed: {book}")
        elif book:
            print("Book already borrowed.")

    def return_book(self, title):
        book = self.search_book(title)
        if book and book.is_borrowed:
            book.is_borrowed = False
            print(f"You returned: {book}")
        elif book:
            print("Book was not borrowed.")


# Demo usage
library = Library()
library.add_book("Python Basics", "John Doe")
library.add_book("AI Fundamentals", "Jane Smith")

library.search_book("Python Basics")
library.borrow_book("Python Basics")
library.return_book("Python Basics")
library.remove_book("AI Fundamentals")
