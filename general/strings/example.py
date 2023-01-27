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
print('ola'[::-1])

# string to list
x = list('my string')

x = 4863.4343091          # example float to format

print(f"{x:.6}")          # f-string version, 4863.43
print("{:.6}".format(x))  # format method version, 4863.43

print(f"{x:.3}")  # 4.86e+03

x = 4863.4343091

print(f"{x:.3f}")  # 4863.434

x = 4863.4343091

print(f"{x:f}")  # 4863.434309 because f defaults to 6 digits

x = 1000000

print(f"{x:,}")  # 1,000,000
print(f"{x:_}")  # 1_000_000

x = 4863.4343091

print(f"{x:,.3f}")  # 4,863.434
print(f"{x:_.3f}")  # 4_863.434

questions = 30
correct_answers = 23

print(f"You got {correct_answers / questions :.2%} correct!")
# You got 76.67% correct!

number_of_files = 3

for file_number in range(1, number_of_files + 1):
	print(f"image{file_number:03}.png")

# image001.png
# image002.png
# image003.png

number_of_files = 3
number_digits = int(input("How many digits are used in the numbering scheme? "))

for file_number in range(1, number_of_files + 1):
	print(f"image{file_number:0{number_digits}}.png")

# image00001.png if user enters 5

base_10 = 231

print(f"This is the number in binary: {base_10 :b}")
# This is the number in binary: 11100111

print(f"This is the number in octal: {base_10 :o}")
# This is the number in octal: 347

print(f"This is the number in hexadecimal: {base_10 :x}")
# This is the number in hexadecimal: e7

print(f"This is the number in uppercase hexadecimal: {base_10 :X}")
# This is the number in uppercase hexadecimal: E7

base_16 = int("E7", base=16)
    
print(f"This is the number in decimal: {base_16 :d}")
# This is the number in decimal: 231

# https://docs.python.org/3/library/string.html#format-specification-mini-language

rgb = (12, 205, 81)
hex_color = "#" + "".join([f"{channel:02x}" for channel in rgb])

print(f"Converted {rgb} to {hex_color}")
# Converted (12, 205, 81) to #0ccd51

format(12, "02x")  # 0c

f"{12:02x}"  # 0c
"{:02x}".format(12)

"Hello, World!".lower()       # "hello, world!"
"Hello, World!".upper()       # "HELLO, WORLD!"
"Hello, World!".capitalize()  # "Hello, world!"
"hello, world!".title()       # "Hello, World!"

"  Hello, World!  ".strip()  # "Hello, World!"

user_name = " ROLF SMITH  ".strip().title()