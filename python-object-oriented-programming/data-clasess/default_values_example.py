from dataclasses import dataclass

@dataclass
class Book:
    # error here because after an arg with default value there is an arg without a default value
    title: str = 'No title'
    author: str = 'No author'
    pages: int
    price: float

book = Book(pages=123,price=123)
print(book)