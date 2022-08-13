class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over"""
        print(f"{self.name} rolled over")

