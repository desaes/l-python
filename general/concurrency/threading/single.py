import threading
import time

def main():
	th = threading.Thread(target=count, args=('elefant', 10))
	th.start() #places the thread in the thread pool
	print("XXX")
	print("YYY")
	th.join() #wait until the thread finishes
	print("ZZZ")

def count(what,numero):
	for n in range(1, numero+1):
		print(f'{n} {what}(s)...')
		time.sleep(1)

if __name__ == "__main__":
	main()
