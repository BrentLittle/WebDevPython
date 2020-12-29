class ClassTest:
    def instanceMethod(self):
        print(f"Called instanceMethod of {self}")
        # used for most things
        # when you want to perform an action inside the object created
        # modify data inside self of object

    @classmethod
    def classMethod(cls):
        print(f"Called classMethod of {cls}")
        # Often used as factories

    @staticmethod
    def staticMethod():
        print(f"Called staticMethod ")
        # to place a method in a class for organization most of the time

test = ClassTest()
test.instanceMethod()
ClassTest.classMethod()
ClassTest.staticMethod()


class Book:
    TYPES = ("hardcover", "paperback")
    def __init__(self, name, bookType, weight):
        self.name = name
        self.bookType = bookType
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.bookType}, weight {self.weight}g>"

    @classmethod    
    def hardcover(cls,name,weight):
        return Book(name, Book.TYPES[0], weight + 100)
        # return cls(name, Book.TYPES[0], weight + 100)
    
    @classmethod
    def paperback(cls,name,weight):
        return Book(name, Book.TYPES[1], weight)
        # return cls(name, Book.TYPES[1], weight)
print(Book.TYPES)

book = Book("Harry Potter", "hardcover", 1500)
book2 = Book.hardcover("Harry Potter", 1500)
book3 = Book.paperback("Python 101", 600)

print(book)
print(book2)
print(book3)