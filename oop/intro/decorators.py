class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    # weekly_salary works like a property/attribute, because it does only return a value
    # and don't accept any values as parameters
    # using @property allows you to use weekly_salary instead of weekly_salary(), in other words, turns a method in a property
    @property
    def weekly_salary(self):
        return self.salary * 37.5

mike = WorkingStudent('Mike', 'MIT', 10)
print(mike.salary)
mike.marks.append(60)
mike.marks.append(70)
print(mike.average())
# calling a method
print(mike.weekly_salary)

# classmethod receives a parameter
class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)

my_obj = Foo()
my_obj.hi()

# staticmethod does not receive a parameter
class Bar:
    @staticmethod
    def hi():
        print('Hello, I don\'t take parameters.')

my_another_obj = Bar()
my_another_obj.hi()

"""
# in this version, you must create the object first to be able to use the from_sum method.
class FixedFloat:
    def __init__(self, amount) -> None:
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'
    
    def from_sum(self, value1, value2):
        return FixedFloat(value1 + value2)
    
number = FixedFloat(18.5746)
new_number = number.from_sum(19.575, 0.789)
print(new_number)

# in the approach bellow, you don't need to do it
class FixedFloat:
    def __init__(self, amount) -> None:
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'
    
    @staticmethod
    def from_sum(value1, value2):
        return FixedFloat(value1 + value2)
    
new_number = FixedFloat.from_sum(19.575, 0.789)
print(new_number)

# in this case, when we call this function, we will receive an output like <FixedFloat 26.79> instead of <FixedFloat 26.79> <Euro €26.79>
class Euro(FixedFloat):
    def __init__(self, amount) -> None:
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'
    
money = Euro.from_sum(16.786,9.999)
print(money)

# to correct it, you must use the @classmethod
"""
class FixedFloat:
    def __init__(self, amount) -> None:
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'
    
    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)
    
class Euro(FixedFloat):
    def __init__(self, amount) -> None:
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'
    
money = Euro.from_sum(16.786,9.999)
print(money)