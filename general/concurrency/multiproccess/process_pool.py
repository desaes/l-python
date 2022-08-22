import multiprocessing
import timeit

PROCS_BY_CORE = 1

def calc(data):
    return data ** 2

def print_proccess_name():
    print(f'Starting process with name: {multiprocessing.current_process().name}')

def main():
    pool_size = multiprocessing.cpu_count() * PROCS_BY_CORE

    print(f'Pool size: {pool_size}')

    # initializer is an optinal parameter
    #pool = multiprocessing.Pool(processes=pool_size, initializer=print_proccess_name())
    pool = multiprocessing.Pool(processes=pool_size)

    inputs = list(range(100_000_000))
    outputs = pool.map(calc, inputs)

    print(f'Outputs: {len(outputs)}')

    pool.close() # tell the pool that we will not map anything more and the pool can be started
    pool.join()

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    stop = timeit.default_timer()
    print('Time: ', stop - start)  