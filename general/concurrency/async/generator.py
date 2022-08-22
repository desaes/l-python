from typing import Generator

def fibo() -> Generator[int, None, None]:
    value: int = 0
    next: int = 1

    while True:
        value, next = next, value + next
        yield value

for n in fibo():
    print(n, end=', ')
    if n > 1000:
        break

print('\nDone')