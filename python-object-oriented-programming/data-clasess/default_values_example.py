from dataclasses import dataclass, field


@dataclass
class Book:
    title: str = 'No title'
    author: str = 'No author'
    pages: int = 123
    price: float = field(default=12)

book = Book()
print(book)
book2 = Book(title="War and peace")
print(book2)