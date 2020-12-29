# Funcitons are callable functions
def hello():
    print("Hello!")
# Python functions must be declared in order to calling them
hello()


def userAgeInSec():
    age = int(input("Enter your age: "))
    seconds = age*365*24*60*60
    print(f"Your age in seconds is {seconds}")
userAgeInSec()

def addFriend():
    friends.append("Rolf")

friends = []
addFriend()
print(friends)