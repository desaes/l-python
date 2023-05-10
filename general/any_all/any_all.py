"""
Any and All

Python provides a built-in function, any, that takes a sequence of boolean values and returns True if any of the values are True. 

all() -> returns true if all elements of an interable are true or even if the interable is empty
any() -> returns true if any element of an interable are true or false if the interable is empty
"""

# All example

print(f' All '.center(50,'#'))

any([False, False, True]) # True
print(all([])) # True List
print(all([1,2,3,4,5])) # True List
print(all([0,1,2,3,4,5])) # False List
print(all((0,1,2,3,4,5))) # False Tuple
print(all({0,1,2,3,4,5})) # False Set
print(all("Test")) # True String

print(any([])) # False
print(any([1,2,3,4,5])) # True
print(any([0,1,2,3,4,5])) # True

any(letter == 't' for letter in 'monty') # True

names = ['Charlie', 'Chloe', 'Charlotte', 'Connor', 'Cara']
print(all([name[0] == 'C' for name in names])) # True

names.append('David')
print(all([name[0] == 'C' for name in names])) # False

# Any example

print(f' Any '.center(50,'#'))

print(any([])) # False List
print(any([0, False, {}, (), []])) # False List
print(any([1,2,3,4,5])) # True List
print(any([0,1,2,3,4,5])) # True List
print(any((0,1,2,3,4,5))) # True Tuple
print(any({0,1,2,3,4,5})) # True Set
print(any("Test")) # True String

names = ['Charlie', 'Chloe', 'Charlotte', 'Connor', 'Cara', 'Tom']
print(any([name[0] == 'C' for name in names])) # True