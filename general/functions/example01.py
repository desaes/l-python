# second arg os optional
def do_something(first_arg, second_arg=''):
    return f"{first_arg}, {second_arg}"

# copying a list to a function to prevent list modification
my_list = [1,2,3,4]
do_something(my_list[:]) # this will give a copy of the list to function

# arbitrary number of arguments
def do_anotherthing(*args):
    for arg in args:
        print(f"- {arg}")

# arbitrary number of arguments + positional arguments
def do_anotherthing(arg1, *args):
    print(arg1)
    for arg in args:
        print(f"- {arg}")

#def build_profile(first, last, **kwargs):
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Marcos', 'Fontana', location='bh', field='it')
print(user_profile) # {'location': 'bh', 'field': 'it', 'first_name': 'Marcos', 'last_name': 'Fontana'}

# importing functions from modules
from module_name import function_name as fn # give function_name fn alias
import module_name as m # give module_name m alias