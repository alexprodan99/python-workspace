from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20,40))

@dataclass
class Book:
    title: str = 'No title'
    author: str = 'No author'
    pages: int = 123
    price: float = field(default_factory=price_func)
    
    

book = Book()
print(book)
book2 = Book(title="War and peace")
print(book2)