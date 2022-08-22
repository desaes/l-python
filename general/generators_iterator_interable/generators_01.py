"""
tuple comprehensions are called generator expression
"""

# Using list comprehentions - any receives a list as parameter
names = ['Charlie', 'Chloe', 'Charlotte', 'Connor', 'Cara', 'Tom']
print(any([name[0] == 'C' for name in names])) # True
ret = [name[0] == 'C' for name in names]
print(ret) # [True, True, True, True, True, False]
print(type(ret)) # <class 'list'>



# Using list generators - pay attention that any does not receive a list
names = ['Charlie', 'Chloe', 'Charlotte', 'Connor', 'Cara', 'Tom']
print(any(name[0] == 'C' for name in names)) # True

# Generators have the same behavior of maps (the data is available in first access)
ret = (name[0] == 'C' for name in names)
print(ret) # <generator object <genexpr> at 0x7f859f37e900> - while list is already created, generators are created on demand (on access)
print(type(ret)) # <class 'generator'>
print(tuple(ret)) # (True, True, True, True, True, False)
print(tuple(ret)) # ()
print(type(ret)) # <class 'generator'>

# Generators are fast than lists because it releases memory after use

from sys import getsizeof # get the size allocated (in bytes) for an object in memory
print(getsizeof('Test')) # 53
names = ['Charlie', 'Chloe', 'Charlotte', 'Connor', 'Cara', 'Tom']
print(getsizeof(names)) # 104
ret = [name[0] == 'C' for name in names]
print(getsizeof(ret)) # 120 for a list
ret = (name[0] == 'C' for name in names)
print(getsizeof([x*10 for x in range(1,10_000)])) # 87616 bytes using list comprehensions
print(getsizeof({x*10 for x in range(1,10_000)})) # 524504 bytes using set comprehensions
print(getsizeof({x: x*10 for x in range(1,10_000)})) # 295000 bytes using dic comprehensions
print(getsizeof(x*10 for x in range(1,10_000))) # 112 bytes using generator expression
print(getsizeof(ret)) # 112 for a list
print(getsizeof(9)) # 28
print(getsizeof(20)) # 28
print(getsizeof(23452345345)) # 32
print(getsizeof(True)) # 28