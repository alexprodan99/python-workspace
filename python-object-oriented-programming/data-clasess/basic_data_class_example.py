from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float
    
    def book_secret(self):
        return f'{self.title}AAA'


book = Book('War and peace','Lev Tolstoi', 123, 2)
print(book) # Book(title='War and peace', author='Lev Tolstoi', pages=123, price=2)
# dataclasess automatically implements eq and repr functions
book2 = Book('War and peace','Lev Tolstoi', 123, 2)
print(book == book2) # True
print(book.book_secret())