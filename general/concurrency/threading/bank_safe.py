import threading
import random
import time
import colorama

from typing import List

lock = threading.RLock()

class Account:
    def __init__(self, balance) -> None:
        self.balance = balance


def create_accounts() -> List[Account]:
    return [
        Account(balance=random.randint(5_000, 10_000)),
        Account(balance=random.randint(5_000, 10_000)),
        Account(balance=random.randint(5_000, 10_000)),
        Account(balance=random.randint(5_000, 10_000)),
        Account(balance=random.randint(5_000, 10_000)),
        Account(balance=random.randint(5_000, 10_000)),
    ]

def transfer(source: Account, destination: Account, value: int):
    if source.balance < value:
        return

    with lock:
        source.balance -= value
        time.sleep(0.001)
        destination.balance += value

def get_accounts(accounts: List[Account]):
    ac1 = random.choice(accounts)
    ac2 = random.choice(accounts)
    while ac1 == ac2:
        ac2 = random.choice(accounts)

    return (ac1, ac2)

def services(accounts, total):
    for _ in range(1,1_000):
        ac1, ac2 = get_accounts(accounts)
        value = random.randint(1,100)
        transfer(ac1, ac2, value)
        validate_bank(accounts, total)

def validate_bank(accounts: List[Account], total):
    with lock:
        current = sum(account.balance for account in accounts)

    if current != total:
        print(colorama.Fore.RED + f'Error: Balance error. $ {current:.2f} vs {total:.2f}', flush=True)
    else:
        print(colorama.Fore.GREEN + f'Info: Balance ok. $ {current:.2f} vs {total:.2f}', flush=True)

def main():
    accounts = create_accounts()
    with lock:    
        total = sum(account.balance for account in accounts)
    print("Begin transfer")

    tasks = [
        threading.Thread(target=services, args=(accounts, total)),
        threading.Thread(target=services, args=(accounts, total)),
        threading.Thread(target=services, args=(accounts, total))
    ]

    [task.start() for task in tasks]
    [task.join() for task in tasks]

    print("End transfer")

    validate_bank(accounts, total)

if __name__ == "__main__":
    main()