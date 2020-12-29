watched = {"Matrix", "Green Book", "Her"}
userWatch = input("Enter something you've watched recently: ")

if userWatch in watched :
     print(f"i've watched {userWatch} too!")
else:
    print(f"I have not watched {userWatch} yet")



# Magic Number App:

number = 7
userIn = input("Enter 'y' if you would like to play: ")

if userIn in ('Y','y'): # instead of using in it is better to trun the user's input inot lower case
    usernum = int(input("Guess our number: "))
    if usernum == number:
        print("You Guessed Correctly")
    elif abs(number - usernum) == 1:
        print("You were one off.")
    else:
        print("You Guessed Incorrectly")