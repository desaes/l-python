import time
from xml.dom.expatbuilder import theDOMImplementation
import colorama

from threading import Thread
from queue import Queue

def data_gen(queue):
    for i in range(1,11):
        print(colorama.Fore.GREEN + f'Data {i} generated.', flush=True)
        time.sleep(2)
        queue.put(i)


def consumer(queue):
    while queue.qsize() > 0:
        value = queue.get() # Reads and also remove the data from the queue
        print(colorama.Fore.RED + f'Data {value*2} consumed.', flush=True)
        time.sleep(1)
        queue.task_done() # Each data read from the queue is a task. When you consume the data or execute the task, you must set it as done

if __name__ == "__main__":
    print(colorama.Fore.WHITE + 'System initialized', flush=True)
    queue = Queue()
    th1 = Thread(target=data_gen, args=(queue,))
    th2 = Thread(target=consumer, args=(queue,))
    th1.start()
    th1.join()
    th2.start()
    th2.join()
