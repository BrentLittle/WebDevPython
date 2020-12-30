# First Class Fucntion means that functions are just variables
# can use them in the same way you would use any other variable
def divide (divid, divis):
    if divis ==0:
        raise ZeroDivisionError("Divisor cannot be 0")
        # This error has a message attached to it
    return divid / divis

def calculate (*values, operator):
    return operator(*values)

result = calculate(20, 4, operator=divide)
print(result)


def search(seq, expected, finder):
    for x in seq:
        if finder(x) == expected:
            return x
    raise RuntimeError(f"Could not find element {expected}.")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

def getName(friend):
    return friend["name"]

print(search(friends, "Rolf Smith", lambda friend: friend["name"]))

print(search(friends, "Rolf Smith", getName))
print(search(friends, "Bob Smith", getName))
