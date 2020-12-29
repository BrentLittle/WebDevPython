# asks users for age
# returns number of months that is

years = int(input("Enter your age: "))
months = years * 12
seconds = years * 365 * 24 * 60 * 60
print(f"You are {years} years old which is {months} months or {seconds} seconds.")