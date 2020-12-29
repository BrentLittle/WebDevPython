def add(x,y):
    print(x+y)    

add(5,3)

def sayHello():
    print("Hello")
# sayHello("Hi") This does not work as sayHello() takes no args

def sayHello(name):
    print(f"Hello {name}")
sayHello("Brent")

# Keyword arguments
def sayHello(name, surname):
    print(f"Hello {name} {surname}")
sayHello(surname = "Brent", name = "Littlefield")



def divide(dividend,divisor):
    if divisor !=0:
        print(dividend/divisor)
    else:
        print("No you can't do that")

# Posiitonal args come first followed by keyword arguments
divide(dividend=15, divisor=0)
divide(15, divisor=0)
divide(divisor=0, dividend=15)