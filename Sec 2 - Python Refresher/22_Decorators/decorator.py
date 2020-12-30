user = {"username": "Brent", "access_level": "guest"}

def getAdminPassword():
    return "1234"

print(getAdminPassword())  # Can do this even though I'm a "guest"

# A way to Secure access to methods
def makeSecure(func):
    def secureFunction():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secureFunction
    
adminPword = makeSecure(getAdminPassword)
print(adminPword())

user["access_level"] = "admin"

adminPword = makeSecure(getAdminPassword)
print(adminPword())