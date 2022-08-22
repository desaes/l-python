from sys import getsizeof

"""

"""

# Generator

def numbers():
    for number in range(1,11):
        yield number

ge1 = numbers()        
print(ge1)

# Generator expression

ge2 = (number for number in range(1,11))
print(ge2)

import time
gen_start = time.time()
print(sum(number for number in range(1000000000)))
gen_elapsed = time.time() - gen_start

list_start = time.time()
print(sum([number for number in range(1000000000)]))
list_elapsed = time.time() - list_start

print(f'generator expression took: {gen_elapsed}')
print(f'list comprehension took: {list_elapsed}')