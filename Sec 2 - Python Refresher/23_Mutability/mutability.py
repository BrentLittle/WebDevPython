# immutable data types are int, float, decimal, bool, string, tuple, and range.
# mutable data types in Python are list, dictionary, set and user-defined classes.

a = []
b = a 

# a and b are names for the same object
print(id(a))
print(id(b))

a.append(35)
print(a)
print(b)

# tuples are immutable
a = ()
b = ()
print(id(a))
print(id(b))

a = a+(15,)
print(id(a))
print(id(b))

a = 8597
b = 8597
print(id(a))
print(id(b))

a = 8598
print(id(a))
print(id(b))

# to make an object immutable do not allow anybody to change 
# the values of it once it is instantiated


#Strings are immutable
a="hello"
b=a
print(id(a))
print(id(b))

a+="World"
print(id(a))
print(id(b))