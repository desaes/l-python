"""
Generators
    generators are iterators
    but not all iterator are generator

    generators can be crated with generator functions
    generator functions use the reserved word yield
    generators can be crated with generator expressions

    Difference among generator functions and generator expressions

+---------------------------------+------------------------------------+
| Functions                       | Generator Functions                |
+---------------------------------+------------------------------------+
| uses return                     | uses yield                         |
+---------------------------------+------------------------------------+
| returns one time                | yield can be called multiple times |
+---------------------------------+------------------------------------+
| retuns no or one value          | returns one generator              |
+---------------------------------+------------------------------------+   
"""

# Generator function example
# This is not a generator, this function creates a generator
def count_to(max):
    counter = 1
    while counter <= max:
        yield counter
        counter = counter + 1


gen = count_to(5)
print(gen)
print(next(gen))
print(list(gen))
print(list(gen))