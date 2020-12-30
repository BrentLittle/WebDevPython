# recommended to use composition rather than inheritance most of the time

class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf has {len(self.books)} books."

# composition is when you want to say a bookshelf has many books associated with it
# a bookshelf is composed of many things plus some books
class Book:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Book {self.name}"

book = Book("Harry Potter")
book2 = Book ("Lord of The Rings")
print(book,book2)
shelf = Bookshelf(book,book2)
print(shelf)