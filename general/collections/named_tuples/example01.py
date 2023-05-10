from collections import namedtuple

"""
class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return '(%g, %g)' % (self.x, self.y)
"""

Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
x, y = p # x = 1, y = 2

# Named tuples provide a quick way to define simple classes. The drawback is that simple
# classes don’t always stay simple. You might decide later that you want to add methods
# to a named tuple. In that case, you could define a new class that inherits from the named
# tuple:

class Pointier(Point):
    pass
    # add more methods here
