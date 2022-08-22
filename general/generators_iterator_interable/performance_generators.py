from sys import getsizeof

def fib_list(max):
    numbers = []
    a, b = 0, 1
    while len(numbers) < max:
        numbers.append(b)
        a, b = b, a + b
    return numbers

#x = fib_list(1000000)
#print(len(x))
#print(x[-1])
#print(getsizeof(x)/1024/1024)

def fib_gen(max):
    a, b, c = 0, 1, 0
    while c < max:
        a, b = b, a + b
        yield a
        c = c + 1
    #return numbers


x = fib_gen(1000000)
print(list(x)[-999990])