# second arg os optional
def do_something(first_arg, second_arg=''):
    return f"{first_arg}, {second_arg}"

# copying a list to a function to prevent list modification
my_list = [1,2,3,4]
do_something(my_list[:]) # this will give a copy of the list to function