"""
set don't allow duplicated values and don't hold order
"""

art_friends = {"Rolf", "Anne"}
science_friends = {"Jen", "Charlie"}

art_friends.add("Jen")
art_friends.remove("Jen") # returns a error if the item does not exist
art_friends.discard("Jen") # don't return a error if the item does not exist
new_set = art_friends.copy() # deep copy 

vegetables = {"carrot", "lettuce", "broccoli", "onion"}
vegetables.update(["potato", "pumpkin"])

print(vegetables)  # {'broccoli', 'lettuce', 'carrot', 'potato', 'pumpkin', 'onion'}

vegetables = {"carrot", "lettuce", "broccoli", "onion"}
random_vegetable = vegetables.pop()  # random, in this case: 'lettuce'

print(vegetables)  # {'broccoli', 'onion', 'carrot'}

"""
Advanced set operations
"""

art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science) # {'Rolf', 'Anne'}
science_but_not_art = science_friends.difference(art_friends)
print(science_but_not_art) # {'Charlie'}
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both) # {'Charlie', 'Rolf', 'Anne'}
art_and_science = art_friends.intersection(science_friends)
print(art_and_science) # {'Jen'}
all_friends = art_friends.union(science_friends)
print(all_friends) # {'Anne', 'Jen', 'Rolf', 'Charlie'}
