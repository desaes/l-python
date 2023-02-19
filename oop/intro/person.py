print(__annotations__)
# {'text': <class 'str'>, 'result': <class 'bool'>, 'name': <class 'str'>, 'weight': <class 'float'>, 'active': <class 'bool'>}

class Person:
    def __init__(self, name: str, age: int, weight: float) -> None:
        self.__name: str = name
        self.__age: int = age
        self.__weight: float = weight

    def walk(self) -> str:
        return f'{self.__name} is walking'

p = Person(name='Marcos', age=43, weight=100)
print(p.__dict__)