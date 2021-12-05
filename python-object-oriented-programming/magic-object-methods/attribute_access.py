class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1
    def __str__(self):
        return f'{self.title} {self.author} {self.price}'

    def __getattribute__(self, name: str):
        if name == 'price':
            p = super().__getattribute__('price')
            d = super().__getattribute__('_discount')
            return p - (p * d)
        return super().__getattribute__(name)
    def __setattr__(self, name, value) :
        if name == 'price':
            if type(value) is not float:
                raise ValueError("The price must be a float")
        return super().__setattr__(name, value)
    # getattr is gonna be called when you try to access attributes that does not exists
    # is called when __getattribute__ fails
    # it can be also used for genereting attributes on the fly
    def __getattr__(self, name):
        return name + " is not here"


book = Book('War and Peace', 'Leo Tolstoi', 23.23)
print(book.price) # each time we are gettign price attribute discount is automatically applied

# error
# book.price = 2
# print(book)
book.price = 2.0
print(book)

book.price = float(20)
print(book)

print(book.random_prop)