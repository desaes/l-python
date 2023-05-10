# A Counter is like a set, except that if an element appears more than once, the Counter
# keeps track of how many times it appears.

from collections import Counter
count = Counter('parrot')
count

# Unlike dictionaries, Counters don’t raise an exception if you access an element that doesn’t
# appear. Instead, they return 0:

count['d'] # 0