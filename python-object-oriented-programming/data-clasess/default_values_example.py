from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int = 321
    price: float = 123.2

 
book = Book('War and peace','Lev Tolstoi')
print(book)