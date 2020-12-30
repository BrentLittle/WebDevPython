from typing import List 

def listAvg(seq: list) -> float:
        # the function takes in a list and returns a float
    return sum(seq)/len(seq)

class Book:
    def __init__(self, name: str, pageCount: int):
        self.name = name
        self.pageCount = pageCount
        
class Bookshelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf has {len(self.books)} books."

print(listAvg([1,2,3,4,5]))