def named(**kwargs): # ** collects keyword arguments into dictionary
    print(kwargs)

named(name="Bob", age=25) # a dictionary is returned


def named(name, age):
    print(name, age)

details = {"name":"Bob", "age":25} # since the key name and age line up 
# with the argument names of the funciton we can unpack the dictionary
named(**details)


def printNice(**kwargs): # Collect args inot dictionary
    named(**kwargs) # unpack dictionary and call named funciton with the unpacked args
    for arg, value in kwargs.items(): # get arg and value of each ditionary item
        print(f"{arg}: {value}") # print the item of the dictionary

printNice(name="Bob", age=25)



def both (*args, **kwargs): # collect positional args inot args and named args into kwargs
    print(args)
    print(kwargs)

both(1,3,5, name="Bob",age=25)



"""
def post(url, data=None, json=None, **kwargs):
    return requet('post',url,data=data,json=json,**kwargs)
"""

def func(**kwargs):
    print(**kwargs)

#func(**"Bob") # Error, Must be mapping (Dictionary)
#func(**None) # Error, Must be mapping (Dictionary)