# Importing a single Class
from dog import Dog
my_dog = Dog("Duke", 6)
print(f"My dog's name is {my_dog.name}")
my_dog.sit()
my_dog.roll_over()

# Importing a single Class
from car import Car
my_fusca = Car("wolkswagen", "fusca", 1970)
my_fusca.update_odometer(23)
my_fusca.read_odometer()
print(my_fusca.get_descriptive_name())



# Importing multiple Classes
from car import Car, ElectricCar

# Importing an Entire Module
import car

# Importing All Classes from a Module (not recommended)
from car import *


# Giving an Alias
from car import ElectricCar as EC
my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
print(my_tesla.battery.describe_battery())
print(my_tesla.battery.get_range())

