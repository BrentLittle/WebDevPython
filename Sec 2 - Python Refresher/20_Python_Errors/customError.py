class TooManyPagesReadError(ValueError):
    pass

class Book:
    def __init__(self, name: str, pageCount: int):
        self.name = name
        self.pageCount = pageCount
        self.pagesRead = 0

    def __repr__(self):
        return(f"<Book {self.name}, read {self.pagesRead} pages out of {self.pageCount}>")
        
    def read(self, pages:int):
        if self.pagesRead + pages > self.pageCount:
            raise TooManyPagesReadError(f"The book only has {self.pageCount} pages and you tried to read {self.pagesRead + pages}")
        self.pagesRead += pages
        print(f"You have read {self.pagesRead} pages out of {self.pageCount}")
        
python = Book("Python",50)
try:
    python.read(35)
    python.read(50)
except TooManyPagesReadError as e:
    print(f"Error: {e}")