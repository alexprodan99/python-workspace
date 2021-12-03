class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = 'This is a secret attribute'
    def get_price(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        return self.price
    def set_discount(self, amount):
        # _ => hint => you know that discount should be internal to the class
        # also if your field's name starts with __ => python interpreter will change it's name so you will get an error trying to access it
        self._discount = amount