from calendar import firstweekday


enemy = {
    'type': 'wolf', 
    'int': 5, 
    'speed': 10, 
    'str': 7
    }

print(enemy['type'].title())

# adding properties to dict
enemy['x_position'] = 10
enemy['y_position'] = 35
enemy['color'] = 'grey'
print(enemy)

# removing key/values
enemy.pop('color')
del enemy['color']
print(enemy)

# using keys in square brackets can cause error if the key does not exist
# use get to avoid the error

speed = enemy.get('sped', 'Speed not available')
print(speed)

# loops

# keys and values
for k, v in enemy.items():
    print(f"key -> {k}, value -> {v}")

friends = {"Rolf": 24, "Adam": 30, "Anne": 27}
for name, age in friends.items():
    print(name, age)    

# keys
# for k in enemy: # same thing of next line.
for k in enemy.keys():
    print(f"key -> {k}")

# in order
for k in sorted(enemy.keys()):
    print(f"key -> {k}")

# values
for v in enemy.values():
    print(f"value -> {v}")     

# unique values
for v in set(enemy.values()):
    print(f"value -> {v}")

friends = [("Rolf", 24), ("Adam", 30), ("Anne",27)]
friend_ages = dict(friends)
print(friend_ages) # {'Rolf': 24, 'Adam': 30, 'Anne': 27}


