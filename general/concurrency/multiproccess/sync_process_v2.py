import multiprocessing

def deposit(balance, lock):
    for _ in range(10_000):
        with lock:
            balance.value = balance.value + 1

def withdraw(balance, lock):
    for _ in range(10_000):
        with lock:
            balance.value = balance.value - 1

def do_transactions(balance, lock):
    proc1 = multiprocessing.Process(target=deposit, args=(balance,lock))
    proc2 = multiprocessing.Process(target=withdraw, args=(balance,lock))

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

if __name__ == '__main__':
    lock = multiprocessing.RLock()
    balance = multiprocessing.Value('i', 100)
    
    print(f'Initial balance: {balance.value}')
    for _ in range(10):
        do_transactions(balance, lock)
    print(f'Final balance: {balance.value}')