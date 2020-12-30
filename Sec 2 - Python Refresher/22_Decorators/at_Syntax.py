import functools

def makeSecure(func): # THIS IS THE DECORATOR
    
    @functools.wraps(func) # THIS ALLOWS THE FUCNTION TO KEEP THE NAME OF THE FUNCITON THAT IS CALLING IT
    def secureFunction(): 
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."
    
    return secureFunction

@makeSecure # WE CAN ADD THE @ SYNTAX TO THIS METHOD TO SECURE IT USING THE METHOD 
            # makeSecure ABOVE
def getAdminPassword():
    return "1234"

user = {"username": "Brent", "access_level": "guest"}
print(getAdminPassword())

user["access_level"] = "admin"
print(getAdminPassword())