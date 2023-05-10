# The collections module also provides defaultdict, which is like a dictionary except that
# if you access a key that doesn’t exist, it can generate a new value on the fly.

# When you create a defaultdict, you provide a function that’s used to create new values. A
# function used to create objects is sometimes called a factory. The built-in functions that
# create lists, sets, and other types can be used as factories:

from collections import defaultdict
d = defaultdict(list)

t = d['new key']
t
[]

# The new list, which we’re calling t, is also added to the dictionary. So if we modify t, the
# change appears in d:

t.append('new value')
d
