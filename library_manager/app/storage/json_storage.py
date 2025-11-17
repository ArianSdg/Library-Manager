import json
import csv
from app.models.book import Book


class Storage:
    def __init__(self, books_file):
        self.books_file = books_file

    def save_books(self, books):
        with open(self.books_file, 'w') as f:
            return json.dump([book.to_dict() for book in books], f, indent=4)

    def load_book(self):
        try:
            with open(self.books_file, 'r') as f:
                return [Book(**book) for book in json.load(f)]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def export_books_csv(self, books, file_path="data/books_export.csv"):
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "Author", "Year", "Borrowed"])
            for book in books:
                writer.writerow([book.title, book.author, book.year, book.is_borrowed])