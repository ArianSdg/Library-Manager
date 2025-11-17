from typing import List
from app.models.book import Book
from app.core.logger import log_activity


class LibraryManager:
    def __init__(self, storage):
        self.storage = storage
        self.books: List[Book] = storage.load_book()

    def add_book(self, title, author, year):
        # Validate title
        if not isinstance(title, str) or title.strip == "":
            return "Invalid input for title."

        # Validate author
        if not isinstance(author, str) or author.strip() == "":
            return "Invalid input for author."

        # Validate year
        if 1000 < year < 2025:
            return "Invalid input for year."

        # Not adding books that already exist
        for b in self.books:
            if b.title.lower() == title.lower() and b.author.lower() == author.lower() and b.year == year:
                log_activity("ADD", b, "Failed - Duplicate")
                return "Can't duplicate the book info!"

        book = Book(title, author, year)
        self.books.append(book)
        self.storage.save_books(self.books)
        log_activity("ADD", book, "Success")

        return f"Book '{title}' added successfully."

    def delete_book(self, title):
        found = False
        for book in self.books[:]:
            if title.lower() == book.title.lower():
                self.books.remove(book)
                log_activity("REMOVE", book, "Success")
                found = True

        self.storage.save_books(self.books)

        if not found:
            log_activity("REMOVE", None, f"Book {title} not found")
            return f"Book {title} not found"
        return f"Book '{title}' removed successfully."

    def borrow_book(self, title):
        for book in self.books:
            if title.lower() == book.title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                self.storage.save_books(self.books)
                log_activity("BORROW", book, "Success")
                return f"Book '{title}' borrowed."
        log_activity("BORROW", None, f"Book {title} not found or already borrowed")
        return f"{title} not found."

    def return_book(self, title):
        for book in self.books:
            if title.lower() == book.title.lower() and book.is_borrowed:
                book.is_borrowed = False
                self.storage.save_books(self.books)
                log_activity("RETURN", book, "Success")
                return f"Book '{title}' returned."
        log_activity("BORROW", None, f"Book {title} not found or already available")
        return f"{title} not found."

    def search_books(self, keyword, borrowed=None):
        result = []
        for book in self.books:
            if (
                (keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower())
                and (borrowed == book.is_borrowed or borrowed is None)
            ):
                result.append(book)
            elif keyword.isdigit() and int(keyword)  == book.year and (borrowed is None or borrowed == book.is_borrowed):
                result.append(book)
        return result

    def list_books(self, sort_by="title"):
        if sort_by.lower() == "title" or sort_by == "1":
            books = sorted(self.books, key=lambda b: b.title.lower())
        elif sort_by.lower() == "author" or sort_by == "2":
            books = sorted(self.books, key=lambda b: b.author.lower())
        elif sort_by.lower() == "year" or sort_by == "3":
            books = sorted(self.books, key=lambda b: b.year)
        elif sort_by.lower() == "borrowed status" or sort_by == "4":
            books = sorted(self.books, key=lambda b: b.is_borrowed)
        else:
            books = self.books

        return books