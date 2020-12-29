#name = input("Please enter your name: ")
#print(name)

#######
# Math with Input
#######
sizeInput = input("How big is your house (sq.ft): ")
squareFeet = int(sizeInput)
sizeMeters = squareFeet / 10.8
print(f"{squareFeet} Sq.ft is equal to {sizeMeters:.2f} Sq.M ")
# :.2f formats the outpu to 2 decimal places