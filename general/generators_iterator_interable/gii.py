"""
Iterator: 
    an object that can be iteracted with
    an object that returns one value each time the next function is called

Iterable:
    an object that will return one iterator when function iter() is called

"""

name = 'Crocodile' # this is an iterable but not an iterator
numbers = [1, 2, 3, 4, 5] # this is an iterable but not an iterator

it1 = iter(name)
it2 = iter(numbers)

print(next(it1))

for it in numbers:
    print(it)