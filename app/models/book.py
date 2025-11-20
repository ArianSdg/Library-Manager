from dataclasses import dataclass


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    count: int

    def to_dict(self):
        return {"id": self.id,
                "title": self.title,
                "author": self.author,
                "year": self.year,
                "count": self.count,
                }

    def __str__(self):
        return f"{self.id} | {self.title} | {self.author} | {self.year} | {self.count}"