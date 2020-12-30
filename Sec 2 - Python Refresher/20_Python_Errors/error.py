def divide (divid, divis):
    if divis ==0:
        raise ZeroDivisionError("Divisor cannot be 0")
        # This error has a message attached to it
    
    return divid / divis

# divide(15,0)

grades = [78,99,85,100]
average = divide (sum(grades), len(grades))
print(f"The average grade is {average}")

# if there are no grades the program does not run properly
grades = []
try:
    average = divide (sum(grades), len(grades))
except ZeroDivisionError as e:
    print("There are no grades in the list")
else:
    print(f"The average grade is {average}")
finally:
    print("We are done")
    
