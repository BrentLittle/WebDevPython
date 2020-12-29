friends = {"Bob" , "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# takes the set friends and removes the set abroad from it
localFriends = friends.difference(abroad)
print(localFriends)

localFriends = abroad.difference(friends)
print(localFriends) # Returns an empty set whihc is notated by set()


local = {"Rolf"}
abroad = {"Bob", "Anne"}

allFriends = local.union(abroad)
print(allFriends)


art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

artOnly = art.difference(science)
scienceOnly =  science.difference(art)
bothArtScience = art.intersection(science)
print(artOnly)
print(scienceOnly)
print(bothArtScience)

## Blog post for set operations
## https://blog.tecladocode.com/python-set-operators/