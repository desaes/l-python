friends = ["Rolf", "Ebert", "Jose"]
friends.append("Lais")
del friends[0]
last = friends.pop() # removes the last item: Lais
second = friends.pop(1) # removes the second item: Ebert
print(friends) # ['Ebert', 'Jose']
print(len(friends))
friends.clear() # clear everything

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

l_1.extend(l_2)

print(l_1)  # [1, 2, 3, 4, 5, 6, 7, 8]