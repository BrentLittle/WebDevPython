student = {"name":"Rolf", "grades":(89,9,93,78,90)}

def average(seq):
    return sum(seq)/len(seq)

print(average(student["grades"]))


class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades
    def averageGrade(self):
        return sum(self.grades)/len(self.grades)

student = Student("Bob", (89,90,93,78,90) )
student2 = Student("Rolf", (89,9,93,78,90) )
print(student.name)
print(student.grades)
print(student.averageGrade())

print(student2.name)
print(student2.grades)
print(student2.averageGrade())

