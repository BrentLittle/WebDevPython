# Define a list
# Can add and remove elements
l = ["Bob" , "Rolf", "Anne"] 

# Define a tuple
# Can NOT add and remove elements
# Cannot be modified after created
t = ("Bob" , "Rolf", "Anne")

# Define a Set
# Cannot have duplicate values
# Does not always keep the order
s = {"Bob" , "Rolf", "Anne"}


print( l[0] )
# print( s[2] ) DOES NOT WORK SINCE THERE IS NO ORDERING

l.append("Smith") # Adds to the end of the list
print( l )

l.remove("Bob") # removes the value from the list
print( l )

s.add("Smith") # Just adds to the set but not in a specific location due to sets having no order
print( s )
s.add("Smith") # If we try to add Smith again it is ignored
print( s )