currencies = 0.8, 1.2
usd, eur = currencies

friends = [("Rolf", 25), ("Anne", 37), ("Charlie",31), ("Bob",22)]

# destructuring
for name, age in friends:
    print(name, age)

# not destructuring

for friend in friends:
    name = friend[0]    
    age  = friend[1]
    print(name, age)

person = ("Bob", 42, "Mechanic")
name, _, profession = person

print(name, profession)  # Bob Mechanic    

head, *tail = [1, 2, 3, 4, 5]

print(head)  # 1
print(tail)  # [2, 3, 4, 5]

head, *middle, tail = [1, 2, 3, 4, 5]

print(head)    # 1
print(middle)  # [2, 3, 4]
print(tail)    # 5

first, second, third, *rest = [1, 2, 3, 4, 5]