import multiprocessing

print(f'Initiating process: {multiprocessing.current_process().name}')

def something(value):
    print(f'doing something with {value} in {multiprocessing.current_process().name}')

def main():
    pc = multiprocessing.Process(target=something, args=('Dog',), name='sub process')
    pc.start()
    pc.join()

if __name__ == "__main__":
    main()
