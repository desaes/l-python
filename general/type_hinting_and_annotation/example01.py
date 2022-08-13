def greeting(name: str) -> str:
    return f"Hello, {name}"

print(greeting('Marcos'))

def header(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50,'#')

print(header('header example 01'))
print(header('header example 02', align=False))

"""
mypy file.py is used to validate the type hinting.
"""

"""
annotations:
"""
text: str
result: bool

import math

def circumference(radius: float) -> float:
    return 2 *math.pi * radius

print(circumference.__annotations__)
# {'radius': <class 'float'>, 'return': <class 'float'>}

name: str = "Marcos"
weight: float = 63.3
active: bool
active = True
id = 1

print(name)
print(weight)

print(__annotations__)
# {'text': <class 'str'>, 'result': <class 'bool'>, 'name': <class 'str'>, 'weight': <class 'float'>, 'active': <class 'bool'>}

class Pessoa:
    def __init__(self, name: str, age: int, weight: float) -> None:
        self.__name: str = name
        self.__age: int = age
        self.__weight: float = weight

    def walk(self) -> str:
        return f'{self.__name} is walking'

p = Pessoa(name='Marcos', age=43, weight=100)
print(p.__dict__)
print(p.walk.__annotations__)
print(p.__init__.__annotations__)