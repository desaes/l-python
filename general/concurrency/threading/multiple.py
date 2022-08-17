import threading
import time

def main():
	threads = [
		threading.Thread(target=count, args=('elefant', 10)),
		threading.Thread(target=count, args=('hole', 8)),
		threading.Thread(target=count, args=('coin', 23)),
		threading.Thread(target=count, args=('duck', 12)),
	]
	[th.start() for th in threads]
	print("XXX")
	print("YYY")
	[th.join() for th in threads]
	print("ZZZ")

def count(what,numero):
	for n in range(1, numero+1):
		print(f'{n} {what}(s)...')
		time.sleep(1)

if __name__ == "__main__":
	main()
