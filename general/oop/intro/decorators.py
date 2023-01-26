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