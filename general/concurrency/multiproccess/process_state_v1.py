import multiprocessing
import time

def func1(val, stat):
    if stat:
        res = val + 10
        stat = False
    else:
        res = val + 20
        val = 200
        stat = True
    print(f'The result of func1 is {res}')
    time.sleep(0.001)

def func2(val, stat):
    if stat:
        res = val + 30
        stat = False
    else:
        res = val + 40
        val = 400
        stat = True
    print(f'The result of func2 is {res}')
    time.sleep(0.001)

def main():
    value = 100
    status = False

    p1 = multiprocessing.Process(target=func1, args=(value, status))
    p2 = multiprocessing.Process(target=func2, args=(value, status))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()

"""
The result of func1 is 120
The result of func2 is 140
"""       