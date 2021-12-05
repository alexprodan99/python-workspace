class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Object to compare with is not a book")
        return self.title == value.title and self.author == value.author and self.price == value.price

    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Object to compare with is not a book")
        return self.price >= value.price

    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Object to compare with is not a book")
        return self.price < value.price

    def __str__(self):
        return f'{self.title} {self.author} {self.price}'
        
    
book1 = Book('War and Peace', "Leo Tolstoi", 23.24)
book2 = Book('War and Peace', "Leo Tolstoi", 23.24)
book3 = Book('War and Peace', "Leo Tolstoi", 20.24)
# without override => FALSE
# ovveride __eq__ => True
print (book1 == book2)

# True
# not overrided __ge__ => error
print (book1 >= book2)

# True
# not overrided __lt__ => error
print (book3 < book1)

# sort books
# because we implemented comparison functions (lt, ge)
books = [book1, book2, book3]
books.sort()
for book in books:
    print (book)