import time

#from concurrent.futures.thread import ThreadPoolExecutor as Executor
from concurrent.futures.process import ProcessPoolExecutor as Executor

def proc1():
    print('[', end='', flush=True)
    for _ in range(1,11):
        print('#', end='', flush=True)
        time.sleep(1)
    print(']', flush=True)
    return 100

if __name__ == '__main__':
    with Executor() as executor:
        ex = executor.submit(proc1)

    print(f'Value returned: {ex.result()}')