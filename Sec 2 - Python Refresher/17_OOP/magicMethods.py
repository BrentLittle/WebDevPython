# __str__ and __repr__

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name} Age: {self.age}"
    def __repr__(self):
        return f"<Person('{self.name}',{self.age})>"

# they are magic methods as you do not need to specifically call them
# Person() is equivalent to Person.__init__()

bob = Person("Bob",35)
print(bob)