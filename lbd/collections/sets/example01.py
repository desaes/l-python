"""
set don't allow duplicated values and don't hold order
"""

art_friends = {"Rolf", "Anne"}
science_friends = {"Jen", "Charlie"}

art_friends.add("Jen")
art_friends.remove("Jen") # returns a error if the item does not exist
art_friends.discard("Jen") # don't return a error if the item does not exist

vegetables = {"carrot", "lettuce", "broccoli", "onion"}
vegetables.update(["potato", "pumpkin"])

print(vegetables)  # {'broccoli', 'lettuce', 'carrot', 'potato', 'pumpkin', 'onion'}

vegetables = {"carrot", "lettuce", "broccoli", "onion"}
random_vegetable = vegetables.pop()  # random, in this case: 'lettuce'

print(vegetables)  # {'broccoli', 'onion', 'carrot'}