import math

def average(numbers):
    try:
        mean = math.fsum(numbers) / len(numbers)
        print(mean)
    except ZeroDivisionError:
        print(0)
    except TypeError:
        print("You provided invalid values!")

"""
In addition to the try and except clauses, we can also use an else clause with our try statements. 
The code under the else clause only runs if no exceptions occur while executing the code in the try clause.
"""    

def average(numbers):
    try:
        mean = math.fsum(numbers) / len(numbers)
    except ZeroDivisionError:
        print(0)
    except TypeError:
        print("You provided invalid values!")
    else: # Executed if no exceptions happens
        print(mean)
    finally: # Always execute
        print(mean)

    

def finally_flex():
    try:
        return
    finally:
        print("You return when I say you can return...")

"""
Nested try.
"""    

def intify(number):
    try:
        return int(number)
    except ValueError:
        try:
            f_number = float(number)
        except ValueError:
            raise ValueError(f"could not convert string to an integer: {number}")
        else:
            return round(f_number)

with open("numbers.txt", "r") as numbers_file:
    numbers = [int(number) for number in numbers_file]

"""
Using from to control and reduce the traceback
There's a lot of information here that I don't really need the user to see, 
because it mostly describes implementation details. I've also defined by own 
custom error message which explains everything the user needs to know about the situation.

To get rid of all of this extra traceback information, we can use another keyword 
in conjunction with raise called from.

from will let us specify a point from which we want to start the traceback information. 
We can do this by referring to an exception by name (remember that we can name exceptions using as). 
Alternatively we can write None in place of an exception name.

None is going to get rid of all of this excess traceback information from this try statement, and just leave us with the most recent exception.
"""    

def intify(number):
    try:
        return int(number)
    except ValueError:
        try:
            f_number = float(number)
        except ValueError:
            raise ValueError(f"could not convert string to an integer: {number}") from None
        else:
            return round(f_number)

with open("numbers.txt", "r") as numbers_file:
    numbers = [int(number) for number in numbers_file]