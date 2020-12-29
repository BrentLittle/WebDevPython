numbers = [1,3,5]
doubled = [x*2 for x in numbers]

print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Sarah", "Jen"]
startsWithS = [friend for friend in friends if friend.startswith("S")]
print (startsWithS)

# two memory locations entirely for these lists
print("Friends: ", id(friends), "startsWithS: ", id(startsWithS))