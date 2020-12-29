number = 7

while True:
    userIn = input("Would you like to play? (Y/n): ")
    
    if userIn == "n":
        break

    usernum = int(input("Guess our number: "))
    if usernum == number:
        print("You guessed correctly")
    elif abs(number - usernum) == 1:
        print("You were one off.")
    else:
        print("You guessed incorrectly")



friends = ["Rolf", "Jen", "Bob", "Anne"]

for name in friends:
    print(f"{name} is my friend")


grades = [35,67,98,100,100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

total = sum(grades)

print(f"The average was: {total/amount}%")
