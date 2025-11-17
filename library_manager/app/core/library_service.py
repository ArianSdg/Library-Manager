from typing import List
from app.models.book import Book


class LibraryManager:
    def __init__(self, storage):
        self.storage = storage
        self.books: List[Book] = storage.load_book()

    def add_book(self, title, author, year):
        # Not adding books that already exist
        for b in self.books:
            if b.title.lower() == title.lower() and b.author.lower() == author.lower() and b.year == year:
                return "Can't duplicate the book info!"

        book = Book(title, author, year)
        self.books.append(book)
        self.storage.save_books(self.books)

    def delete_book(self, title):
        self.books = [book for book in self.books if book.title.lower() != title.lower()]
        self.storage.save_books(self.books)

    def borrow_book(self, title):
        for book in self.books:
            if title.lower() == book.title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                self.storage.save_books(self.books)
                return f"Book '{title}' borrowed."
        return f"{title} not found."

    def return_book(self, title):
        for book in self.books:
            if title.lower() == book.title.lower() and book.is_borrowed:
                book.is_borrowed = False
                self.storage.save_books(self.books)
                return f"Book '{title}' returned."
        return f"{title} not found."

    def search_books(self, keyword):
        result = []
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                result.append(book)
        return result

    def list_books(self):
        result = ""
        i = 1
        for book in self.books:
            result += f"{i}. {book.__str__()}\n"
            i += 1
        return result