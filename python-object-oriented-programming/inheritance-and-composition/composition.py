class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        
        self.author = author
        self.chapters = []
    
    def add_chapter(self, chapter):
        self.chapters.append(chapter)
        
    def get_book_page_count(self):
        res = 0
        for chapter in self.chapters:
            res += chapter.pages
        return res
        
class Author:
    def __init__(self, author_fname, author_lname):
        self.author_fname = author_fname
        self.author_lname = author_lname
    def __str__(self):
        return f'{self.author_fname} {self.author_lname}'

class Chapter:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages
    def __str__(self):
        return f'{self.name} {self.pages}'

author = Author('Leo', 'Tolstoy')
book = Book('War and Peace', 39.0, author)
chapter1 = Chapter('Chapter1', 123)
chapter2 = Chapter('Chapter2', 200)

book.add_chapter(chapter1)
book.add_chapter(chapter2)

print(book.author)
print(book.chapters)
print(book.get_book_page_count())