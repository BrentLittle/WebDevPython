# Funcitons without a name

# exclusively used to operate on inputs and return outputs
# almost never used to perform actions
# Typically used for very simple operations and nothing too complicated
# usually singled lined sure to complicated syntax

def add(x,y):
    return x + y
print(add(5,7))


def double(x):
    return x*2

seq = [1,3,5,7,9]

doubled = [double(x) for x in seq]
print(doubled)

doubled = [(lambda x: x*2)(x) for x in seq]
print(doubled)

doubled = list(map(lambda x: x*2, seq))
print(doubled)