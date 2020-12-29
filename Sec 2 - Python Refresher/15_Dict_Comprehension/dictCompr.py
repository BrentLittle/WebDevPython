users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longpassword"),
    (3, "username", "1234")
]

userMapping = {user[1]:user for user in users}

print(userMapping)
print(userMapping["Bob"])

usernameIn = input("Enter your username: ")
passwordIn = input("Enter your password: ")

_, username, password = userMapping[usernameIn]

if passwordIn == password:
    print("Details correct!")