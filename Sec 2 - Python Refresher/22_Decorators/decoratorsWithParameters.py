import functools


def makeSecure(accessLevel):
    
    def decorator(func): # THIS IS THE DECORATOR

        @functools.wraps(func) # THIS ALLOWS THE FUCNTION TO KEEP THE NAME OF THE FUNCITON THAT IS CALLING IT
        def secureFunction(*args, **kwargs): # THIS ALLOWS FOR UNLIMITED PARAMTERS TO BE SENT TO THE SECURE FUNCTION
            if user["access_level"] == accessLevel:
                return func(*args, **kwargs) # CALL THE SECURED FUCNTION WITH UNLIMITED ARGUMENTS IF NEEDED
            else:
                return f"No {accessLevel} permissions for {user['username']}."
    
        return secureFunction
    
    return decorator

@makeSecure("admin") # function call happens first and then the result is applied to the functin below
def getAdminPassword():
    return "admin: 1234"

@makeSecure("user")
def getDashboardPassword():
    return "user: userPassword"

user = {"username": "Brent", "access_level": "guest"}
print(f"\n {user}")
print(getAdminPassword())
print(getDashboardPassword())

user = {"username": "Littlefield", "access_level": "user"}
print(f"\n {user}")
print(getAdminPassword())
print(getDashboardPassword())

user = {"username": "Kat", "access_level": "admin"}
print(f"\n {user}")
print(getAdminPassword())
print(getDashboardPassword())