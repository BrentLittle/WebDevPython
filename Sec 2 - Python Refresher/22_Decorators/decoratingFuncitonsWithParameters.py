import functools

def makeSecure(func): # THIS IS THE DECORATOR
    
    @functools.wraps(func) # THIS ALLOWS THE FUCNTION TO KEEP THE NAME OF THE FUNCITON THAT IS CALLING IT
    def secureFunction(*args, **kwargs): # THIS ALLOWS FOR UNLIMITED PARAMTERS TO BE SENT TO THE SECURE FUNCTION
        if user["access_level"] == "admin":
            return func(*args, **kwargs) # CALL THE SECURED FUCNTION WITH UNLIMITED ARGUMENTS IF NEEDED
        else:
            return f"No admin permissions for {user['username']}."
    
    return secureFunction

@makeSecure # WE CAN ADD THE @ SYNTAX TO THIS METHOD TO SECURE IT USING THE METHOD 
            # makeSecure ABOVE
def getPassword(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "SuperSecurePassword"

user = {"username": "Brent", "access_level": "guest"}
print(getPassword("admin")) # THIS METHOD MUST BE CALLED USING THE CORRECT AGUMENTS FOR THE SECURED FUNCITON

user["access_level"] = "admin"
print(getPassword("billing"))