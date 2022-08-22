import multiprocessing
import timeit
import time

PROCS_BY_CORE = 1

class Calc:
    def __init__(self, data):
        self.data = data
        calc(self.data)
        time.sleep(0.5)

def calc(data):
    return data ** 2

def main():
    pool_size = multiprocessing.cpu_count() * PROCS_BY_CORE

    print(f'Pool size: {pool_size}')

    pool = multiprocessing.Pool(processes=pool_size)

    #inputs = list(range(100_000_000))
    inputs = list(range(100))
    outputs = pool.map(Calc, inputs)

    print(f'Outputs: {len(outputs)}')

    pool.close() # tell the pool that we will not map anything more and the pool can be started
    pool.join()

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    stop = timeit.default_timer()
    print('Time: ', stop - start)  