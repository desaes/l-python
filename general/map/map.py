"""
map

Used to map values to functions
"""

import math
import time

def area(r):
    """
    Calculate area of a circle with the given radius (r)
    """
    #return float(f'{math.pi * (r ** 2):.2f}')
    return math.pi * (r ** 2)

print(area(2))

radius = [2, 5, 7.1, 0.3, 10, 44]

# Usual way
areas = []
for r in radius:
    areas.append(area(r))

print(areas)

# Using map
# map receive 2 parameters, first is the function and second is the interable
areas = map(area, radius)
print(list(areas))


# Using map with lambda
print(list(map(lambda r: math.pi * (r ** 2), radius)))

# Another example
cities = [('Berlim', 29), ('Buenos Aires',19), ('Los Angeles', 35), ('Tokyo', 10), ('New Yoork', 22)]
# Lambda
c_to_f = lambda data: (data[0],(9/5) * data[1] + 32)
print(list(map(c_to_f, cities)))