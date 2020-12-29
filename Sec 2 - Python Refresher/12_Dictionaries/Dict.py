friendAges = {"Rolf": 24, "Adam":30, "Anne":27}
print(friendAges["Adam"])

friendAges["Bob"] = 20
print(friendAges)

friendAges["Rolf"] = 20
print(friendAges)


friends = [
    {"name":"Rolf", "age": 24},
    {"name":"Adam", "age": 30},
    {"name":"Anne", "age": 27}
]
print(friends)
print(friends[1]["name"])
print(friends[2]["age"])


attendance = {"Rolf": 96, "Bob": 80, "Anne" :100}
for student,attended in attendance.items() :
    print(f"{student}: {attended}")


if "Bob" in attendance:
    print(f"Bob: {attendance['Bob']}")
else:
    print("Bob is not a student")



attendVals = attendance.values()
print(sum(attendVals)/ len(attendVals))
