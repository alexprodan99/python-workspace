class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    # __str__ => showing info about object (user friendly)
    def __str__(self):
        return f'{self.title} by {self.author} costs {self.price}'
    # __repr__ => debugging purposes
    def __repr__(self):
        return f'title={self.title}, author={self.author}, price={self.price}'
    
book = Book('War and Peace', "Leo Tolstoi", 23.55)
# how actually works
# if just repr is defined str(obj) = repr(object)
# else will use __str__
# if just __str__ is defined repr(object) != str(obj) (will be default one)

# checkings order
# __repr__ -> __str__

print(book) # __str__ is defined so use it
print(str(book))
print(repr(book))
