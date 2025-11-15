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
        self.books = [book for book in self.books if book.title != title]
        self.save_books()

    def borrow_book(self, title):
        return []

    def return_book(self, title):
        return []

    def search_books(self, keyword):
        return []

    def save_books(self):
        with open(self.books_file, 'w') as f:
            return json.dump([book.__dict__ for book in self.books], f, indent=4)


    def load_book(self, books_file):
        return []

manager = LibraryManager('books.json')
manager.add_book("arian", "arian", "1995")
manager.add_book("amir", "arian", "1995")
manager.add_book("azar", "arian", "1995")
print(manager.delete_book("amir"))