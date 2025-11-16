import json
from models.book import Book


class Storage:
    def __init__(self, books_file):
        self.books_file = books_file

    def save_books(self, books):
        with open(self.books_file, 'w') as f:
            return json.dump([book.__dict__ for book in books], f, indent=4)

    def load_book(self):
        try:
            with open(self.books_file, 'r') as f:
                return [Book(**book) for book in json.load(f)]
        except (json.JSONDecodeError, FileNotFoundError):
            return []