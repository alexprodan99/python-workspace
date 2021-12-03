class Book:
    # static fields
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    
    __book_list = None
    def __init__(self, title, author, pages, price, book_type = "EBOOK"):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = 'This is a secret attribute'
        if book_type not in Book.BOOK_TYPES:
            raise ValueError('Invalid booktype provided')
        self.book_type = book_type
    
    # not self = instance as argument => pass class
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES;

    @staticmethod
    def get_book_list():
        if Book.__book_list == None:
            Book.__book_list = []
        return Book.__book_list
    
    def get_price(self):
        # check if user provided an attribute that wasn't included in __init__
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        return self.price
    def set_discount(self, amount):
        # _ => hint => you know that discount should be internal to the class
        # also if your field's name starts with __ => python interpreter will change it's name so you will get an error trying to access it
        self._discount = amount