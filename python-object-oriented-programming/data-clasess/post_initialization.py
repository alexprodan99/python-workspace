from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float
    
    # called after __init__
    # creates attributes after initialization of required ones
    def __post_init__(self):
        self.description = f'{self.title} by {self.author}, {self.pages} pages'

book = Book('War and peace','Lev Tolstoi', 123, 2)
print(book.description)