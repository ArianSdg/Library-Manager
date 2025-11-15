

class Book:
    def __init__(self, title, author, year, is_borrowed=False):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = is_borrowed

class LibraryManager:
    def add_book(self, title, author, year):

    def delete_book(self, title):

    def borrow_book(self, title):

    def return_book(self, title):

    def search_books(self, keyword):

    def save_books(self):

    def load_book(self):
