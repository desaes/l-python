import threading, time

def count(what,numero):
	for n in range(1, numero+1):
		print(f'{n} {what}(s)...')
		time.sleep(1)

th = threading.Thread(target=count, args=('elephant', 10))

lock = th.Lock()

### Unsafe lock
# Lock
lock.acquire()

# Oper
# If any exception happens here, the lock will never be released.

# Unlock
lock.release()

### Safe lock with exception handling
# Lock
lock.acquire()
try:
    pass # oper
except Exception as e:
    pass # exception handling
finally:
    lock.release()

### Safe lock with with - acquire and release will be used automatically by with
with lock:
    pass # oper


### Check if lock is free or not    
if lock.acquire(False):
    pass # Lock is free and I can lock
else:
    pass # I will do another thing until I can lock

### Never call acquire 2 times or the second one will be waiting forever using the Lock()
lock.acquire()
lock.acquire() # this instruction will wait forever

### Always use RLock instead of lock because it will never lock the same thread
lock = th.RLock()