print(bool(0))              # False
print(bool(6))              # True

print(bool("Caterpillar"))  # True
print(bool(""))             # False

print(bool([]))             # False
print(bool([0, 1, 2, 3]))   # True

print(bool(True))           # True
print(bool(False))          # False


print(5 < 10)     # True
print(5 > 10)     # False
print(10 > 10)    # False
print("A" < "a")  # True

print(10 > 10)   # False
print(10 >= 10)  # True

print(0 == "0")                # False
print(0 == 0)                  # True
print(7 == 7.0)                # True
print("Hello" == "Hello!")     # False
print([1, 2, 3] == [1, 2, 3])  # True

print(0 != "0")         # True
print(0 != 0)           # False
print("Hello" != "Hi")  # True

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))  # 139806639351360
print(id(b))  # 139806638418944

print(a == b)  # True
print(a is b)  # False

a = [1, 2, 3]
b = a

print(id(a))  # 139685763327296
print(id(b))  # 139685763327296

print(a == b)  # True
print(a is b)  # True