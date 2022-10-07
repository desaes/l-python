from calendar import firstweekday

w = {}.fromkeys(range(1,11), 'valor')
# w => {1: 'valor', 2: 'valor', 3: 'valor', 4: 'valor', 5: 'valor', 6: 'valor', 7: 'valor', 8: 'valor', 9: 'valor', 10: 'valor'}

x = {}.fromkeys('a', 'b')
# x => {'a': 'b'}

y = {}.fromkeys('abcde', 'vwxyz')
# y => {'a': 'vwxyz', 'b': 'vwxyz', 'c': 'vwxyz', 'd': 'vwxyz', 'e': 'vwxyz'}

z = {}.fromkeys('test', 'vwxyz')
# z => {'t': 'vwxyz', 'e': 'vwxyz', 's': 'vwxyz'} # t can't be dup

enemy_far_less_common = {}.fromkeys(['type', 'int', 'speed', 'str'], 'unknow')
# enemy_far_less_common => {'type': 'unknow', 'int': 'unknow', 'speed': 'unknow', 'str': 'unknow'}

enemy_less_common = dict(type='spider', int=2, speed=10, str=4)

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

# clear the dict
enemy.clear()

# copy a dict, deep copy
new = enemy.copy()


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


