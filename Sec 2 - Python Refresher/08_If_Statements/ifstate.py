dayOfWeek = input("What day of the week is it? ").lower()

print(dayOfWeek == "Monday")


### BAD CODE Use ELSE
if (dayOfWeek == "monday"):
    print ("It is Monday!")
if (dayOfWeek != "monday"):   
    print("Keep on going!")


if (dayOfWeek == "monday"):
    print ("It is Monday!")
elif (dayOfWeek == "tuesday"):
    print ("It is Tuesday!")
else:
    print("Keep on going!")

