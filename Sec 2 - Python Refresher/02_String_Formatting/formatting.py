"""
### Lecture: String Formatting
"""
########
# f-strings in Python
########
name = "Bob"
greeting = f"Hello, {name}" #embedds the value that the variable name had at the time into greeting

print(greeting)

name = "Rolf"

print(greeting) # This will not return Hello,Rolg but Hello, Bob as the value of name at assignment of greeting was Bob

# What is nice about f-string is that we can directly print it and use the variable at the latest point in time
print(f"Hello, {name}")


########
#  Template Strings with .format()
########
name = "Bob"
greeting = "Hello, {}"
withName = greeting.format(name)

# .format() replaces the curly braces with the value of wha tis passed to the function
print(withName)
# Can reuse template as well to create different strings

longString = "Hello, {}. Today is {}."
formatted = longString.format("Rolf","Monday")
print(formatted)
print(longString.format("Rolf","Monday"))