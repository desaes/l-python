numbers = [0, 1, 2, 3, 4]

#double_numbers = [x*2 for x in numbers]
double_numbers = [x*2 for x in range(5)]

print(double_numbers)

ages = [22, 35, 27, 21, 20]
odds = [age for age in ages if age % 2 == 1]
print(odds)

# -- with strings --

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = [f.lower() for f in friends]

present_friends = [
    name.capitalize() for name in guests if name.lower() in friends_lower
]

# -- nested list comprehensions --
# Don't do this, because it's almost completely unreadable.
# Splitting things out into variables is better.

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

present_friends = [
    name.capitalize() for name in guests if name.lower() in [f.lower() for f in friends]
]
print(present_friends)
