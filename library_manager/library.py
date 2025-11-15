from typing import List
from dataclasses import dataclass
import json


@dataclass
class Book:
    def __init__(self, title, author, year: int, is_borrowed=False):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = is_borrowed


class LibraryManager:
    def __init__(self, books_file: str):
        self.books_file = books_file
        self.books: List[Book] = self.load_book(books_file)

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)
        self.save_books()

    def delete_book(self, title):
        self.books = [book for book in self.books if book.title.lower() != title.lower()]
        self.save_books()

    def borrow_book(self, title):
        for book in self.books:
            if title.lower() == book.title.lower():
                if book.is_borrowed:
                    print(f"Book '{book.title}' is already borrowed.")
                else:
                    book.is_borrowed = True
        self.save_books()

    def return_book(self, title):
        for book in self.books:
            if title.lower() == book.title.lower():
                if book.is_borrowed:
                    book.is_borrowed = False
                else:
                    print(f"Book '{book.title}' is already in the library.")
        self.save_books()

    def search_books(self, keyword):
        return []

    def save_books(self):
        with open(self.books_file, 'w') as f:
            return json.dump([book.__dict__ for book in self.books], f, indent=4)


    def load_book(self, books_file):
        try:
            with open(books_file, 'r') as f:
                return [Book(**book) for book in json.load(f)]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

manager = LibraryManager('books.json')
manager.add_book("arian", "arian", "1995")
manager.add_book("amir", "arian", "1995")
manager.add_book("azar", "arian", "1995")
print(manager.delete_book("amir"))
manager.borrow_book("azar")