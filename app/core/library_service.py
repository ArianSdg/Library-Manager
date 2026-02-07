from typing import List
from app.models.book import Book
from app.core.logger import log_activity


class LibraryManager:
    def __init__(self, storage):
        self.storage = storage
        self.books: List[Book] = storage.load_book()
        self.next_id = max([b.id for b in self.books], default=0) + 1

    def add_book(self, title, author, year, count):
        # Validate title
        if not isinstance(title, str) or not title.strip == "":
            return "Invalid input for title."

        # Validate author
        if not isinstance(author, str) or author.strip() == "":
            return "Invalid input for author."

        # Validate year
        if not (1000 <= year <= 2025):
            return "Invalid input for year."

        # Not adding books that already exist
        for b in self.books:
            if b.title.lower() == title.lower() and b.author.lower() == author.lower() and b.year == year:
                log_activity("ADD", b, "Failed - Duplicate")
                return "Can't duplicate the book info!"

        book = Book(self.next_id, title, author, year, count)

        self.books.append(book)
        self.storage.save_books(self.books)
        self.storage.export_books_csv(self.books)
        log_activity("ADD", book, "Success")

        return f"Book '{title}' added successfully."

    def delete_book(self, id):
        found = False
        for book in self.books[:]:
            if id == book.id:
                self.books.remove(book)
                log_activity("REMOVE", book, "Success")
                found = True

        self.storage.save_books(self.books)
        self.storage.export_books_csv(self.books)

        if not found:
            log_activity("REMOVE", None, f"Book with '{id}' ID not found")
            return f"Book with '{id}' ID not found."
        return f"Book with '{id}' ID removed successfully."

    def borrow_book(self, id):
        for book in self.books:
            if id == book.id:
                if book.available() > 0:
                    book.borrowed += 1
                    self.storage.save_books(self.books)
                    self.storage.export_books_csv(self.books)
                    log_activity("BORROW", book, "Success")
                    return f"Book with '{id}' ID borrowed."
                else:
                    log_activity("BORROW", book, f"Failed - No copies found.")
                    return "No copies found"

        log_activity("BORROW", None, f"Book with '{id}' ID not found.")
        return f"Book with '{id}' ID not found."

    def return_book(self, id):
        for book in self.books:
            if id == book.id:
                if book.borrowed > 0:
                    book.borrowed -= 1
                    self.storage.save_books(self.books)
                    self.storage.export_books_csv(self.books)
                    log_activity("RETURN", book, "Success")
                    return f"Book with '{id}' ID returned."
                else:
                    log_activity("RETURN", book, f"Book with {id} ID is not Borrowed.")
                    return f"Book is not Borrowed."

        log_activity("BORROW", None, f"Book with '{id}' ID not found.")
        return f"Book with '{id}' ID not found."

    def search_books(self, keyword):
        result = []
        for book in self.books:
            if (
                (keyword.lower() in book.title.lower()
                or keyword.lower() in book.author.lower()
                or keyword.isdigit() and int(keyword) == book.year)
            ):
                result.append(book)
        return result

    def list_books(self, sort_by="id"):
        if sort_by.lower() == "title" or sort_by == "1":
            books = sorted(self.books, key=lambda b: b.title.lower())
        elif sort_by.lower() == "author" or sort_by == "2":
            books = sorted(self.books, key=lambda b: b.author.lower())
        elif sort_by.lower() == "year" or sort_by == "3":
            books = sorted(self.books, key=lambda b: b.year)
        elif sort_by.lower() == "borrowed status" or sort_by == "4":
            books = sorted(self.books, key=lambda b: b.is_borrowed)
        elif sort_by.lower() == "id" or sort_by == "0":
            books = sorted(self.books, key=lambda b: b.id)

        return books