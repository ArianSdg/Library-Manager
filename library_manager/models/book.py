from dataclasses import dataclass


@dataclass
class Book:
    def __init__(self, title, author, year: int, is_borrowed=False):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = is_borrowed

    def to_dict(self):
        return {"title": self.title,
                "author": self.author,
                "year": self.year,
                "is_borrowed": self.is_borrowed,
                }