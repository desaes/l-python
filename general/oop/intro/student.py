"""
# No OOP

my_student = {
    'name': 'Mike',
    'grades': [70,88,90,99]
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])

print(average_grade(my_student))

# Converting to OOP

class Student:
    def __init__(self, name, grades) -> None:
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Mark', [70,88,90,99])
print(student_one.average())
print(student_one.name)
print(student_one.__class__)

# Everything is an object

print("hi".__class__)
print([1,2,3].__class__)
"""

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


