from typing import List


class Student:
    def __init__(self, name: str, grades: List[int] = []):  # This is bad! never make a parameter equal to a mutable value by default
                                                            # this default valued mutable parameter evaluate when the function is defined NOT when the function is called
        self.name = name
        self.grades = grades

    def takeExam(self, result):
        self.grades.append(result)
        
bob = Student("Bob")
rolf = Student("Rolf")
bob.takeExam(90)
print(bob.grades)
print(rolf.grades)  # Bob's Exam grade is now apart of Rolf's
                    # the data is not separated between objects
                    # they are both refering to the SAME LIST
                    
                    
from typing import List

class Student:
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []  # New list created if one isn't passed

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)  # Now it's empty.



from typing import List, Optional

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []  # New list created if one isn't passed

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)  # Now it's empty.