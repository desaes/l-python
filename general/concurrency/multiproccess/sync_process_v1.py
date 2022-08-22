import multiprocessing

def deposit(balance):
    for _ in range(10_000):
        balance.value = balance.value + 1

def withdraw(balance):
    for _ in range(10_000):
        balance.value = balance.value - 1

def do_transactions(balance):
    proc1 = multiprocessing.Process(target=deposit, args=(balance,))
    proc2 = multiprocessing.Process(target=withdraw, args=(balance,))

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

if __name__ == '__main__':
    balance = multiprocessing.Value('i', 100)
    
    print(f'Initial balance: {balance.value}')
    for _ in range(10):
        do_transactions(balance)
    print(f'Final balance: {balance.value}')