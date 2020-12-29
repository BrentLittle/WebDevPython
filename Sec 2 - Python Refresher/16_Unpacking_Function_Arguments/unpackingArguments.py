def multiply(*args):
    #print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total
print(multiply(1,2,5,7,9))


def add(x,y):
    return x+y

nums = [3,5]
print(add(*nums)) # This breaks the nums variable down inot x=3 and y=5. 
# need to make sure the list has the appropriate number of elements as the 
# function has arguments or there will be errors


nums = {"x":15, "y":25}
print(add(x=nums["x"], y=nums["y"]))
print(add(**nums))

def apply(*args,operator): # operator is a required named argument
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator for apply()"
print(apply(1,3,6,7, operator="+")) # must pass in a named arg at the end
print(apply(1,3,6,7, operator="*"))
print(apply(1,3,6,7, operator="/")) 
