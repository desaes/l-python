friends = ["Rolf", "Ebert", "Jose"]
# check if element is in a list
'Ebert' in friends # True
friends.append("Lais")
del friends[0]
last_item = friends.pop() # removes the last item: Lais
second = friends.pop(1) # removes the second item: Ebert
print(friends) # ['Ebert', 'Jose']
print(len(friends))
friends.insert(0, 'Somebody')
friends_sorted = sorted(friends) # sort a list without changing the original
friends.sort() # permanently sort a list
friends.sort(reverse=True) # permanently sort a list
friends.reverse() # permanently reverse a list
friends[::-1] # also reverse a list
lcopy = friends.copy() # copy a list
lcopy = friends[::] # copy a list
friends.clear() # clear everything

l = [1, 2, 2, 3, 3, 4, 4, 4, 5]
l.count(2) # count the number of items in the list that matches with the given parameter 

len(friends) # lenght of a list

friends = [
    ["Rolf", 24],
    ["Ebert", 50], 
    ["Jose", 10]
    ]

friends.remove(["Rolf", 24])    

for friend in friends:
    print(friend[0])

l_1 = [1,2,3,4]    
l_2 = [5,6,7,8]


new_list = l_1 + l_2
print(new_list) # [1, 2, 3, 4, 5, 6, 7, 8]

# extend only accepts iterable as parameter. same of l_1 + l_2
l_1.extend(l_2)

# insert a new value in the list at given position
l_1.insert(2, 'new value')

print(l_1)  # [1, 2, 3, 4, 5, 6, 7, 8]

# remove all entries that match in a list
pets = ['cat', 'dog', 'bird', 'turtle', 'cat']
while 'cat' in pets:
    pets.remove('cat')

my_number_list = list(range(1,1001))

# list comprehensions
squares = [value**2 for value in range(1,11)] # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# slicing
squares[0:3]  # [1, 4, 9]
squares[:3]   # [1, 4, 9]
squares[1:4]  # [4, 9, 16]
squares[4:]   # [25, 36, 49, 64, 81, 100]
squares[-3:]  # [64, 81, 100]
squares[:-3]  # [1, 4, 9, 16, 25, 36, 49]

# copy a list
new_list = squares[:]

# average of a list
grades = [80, 75, 90, 100]
print(sum(grades)/len(grades))

# join
friends = ["Rolf", "Anne", "Charlie"]
comma_separated = ", ".join(friends)
print(f"My friends are {comma_separated}")

# string to list
x = list('my string')