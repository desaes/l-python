"""
String oper examples
"""
var = "one example"
var1 = "another example"
print(f"this is {var}.")
print("this is {}.".format(var1))
print("this is {variable}.".format(variable=var1))


def header(text, align=True):
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50,'#')

print(header('header example 01'))
print(header('header example 02', align=False))

# reverse the string
print(str[::-1])

# string to list
x = list('my string')