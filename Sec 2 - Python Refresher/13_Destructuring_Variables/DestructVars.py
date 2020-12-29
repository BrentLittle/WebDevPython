t = (5,11)
x , y = t
print(x,y)

attendance = {"Rolf": 96, "Bob": 80, "Anne" :100}
print(list(attendance.items()))

for t in attendance.items() :
    print(t)
# print(f"{student}: {attended}")

for student, attended in attendance.items() :
    print(f"{student}: {attended}")

# Blog post: https://blog.tecladocode.com/destructuring-in-python/

people = [("Bob",42,"Mechanic"), ("James",24,"Artist"), ("Harry",32,"Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")
for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")


person = ("Bob",42,"Mechanic")
name, _, profession = person
print(name, _, profession)

head, two,  *tail = [1,2,3,4,5]
print(head)
print(two)
print(tail)

*head, two, tail = [1,2,3,4,5]
print(head)
print(two)
print(tail)