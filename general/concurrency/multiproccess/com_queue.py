import multiprocessing
import random

"""
Methods of queue with threading.Queue:
    qsize()
    put()
    get()
    empty()
    full()
    task_done()
    join()

Methods of queue with multiprocessing.Queue:
    qsize()
    put()
    get()
    empty()
    full()
    - task_done() -> does not exist
    - join()      -> does not exist

Methods of queue with multiprocessing.JoinableQueue:
    qsize()
    put()
    get()
    empty()
    full()
    task_done()
    join()
"""

def ping(queue):
    queue.put('Ping')

def pong(queue):
    msg = queue.get()
    print(f'Pong: {msg}')

def main():
    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=ping, args=(queue,))
    p2 = multiprocessing.Process(target=pong, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()