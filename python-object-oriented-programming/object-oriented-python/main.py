from book import Book

b1 = Book('Brave New World', 'Leo Tolstoy', 1225, 39.95)
b2 = Book('War and Peace', 'Leo Tolstoy', 1245, 29.95)


print(b1)
print(b1.title) # title is public
print(b1.get_price())
print(b2.get_price())
b2.set_discount(0.25)
# print(b2._discount) => not an error, but you shouldn't access internal variables
print(b2.get_price())
# name mangling
# print(b2.__secret) => error
# print(b2._Book__secret) # you will access __secret, but you shouldn't

print (type(b1) == type(b2)) # True
print (isinstance(b1, Book)) # True

print (f'BOOK_TYPES={Book.get_book_types()}')

books = Book.get_book_list()
books.append(b1)
books.append(b2)
print(books)