from dataclasses import dataclass

@dataclass
class Book:
    title: str = 'No title'
    author: str = 'No author'
    pages: int = 123
    price: float = 12

book = Book()
print(book)