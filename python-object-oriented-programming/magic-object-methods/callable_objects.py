class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def __str__(self):
        return f'{self.title} {self.author} {self.price}'

    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

book = Book('War and Peace', 'Lev Tolstoi', 23.24)
print(book)

book('The Catcher', 'JD Salinger', 12.32)
print(book)

book(title='JSD', author='JDS', price=232.2)
print(book)