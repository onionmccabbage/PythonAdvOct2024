import threading

# All threads on a particular Python execution share the same resources
# There is ONE copy of Python, ONE set of data (memory, DB, I/O etc.)
# Each thread is given its own heap of memory once it is running
# This means other threads cannot access the objects created in a child thread

# We may use a lock to make shared resources 'thread safe'

# here is a global asset
counter = 0
lock = threading.Lock()

def workerA():
    '''this worker will access the global counter to increment it'''
    global counter
    lock.acquire() # we have exclusive access to the lock
    while counter < 10:
        counter+=1
        print(f'Worker A increments the counter to {counter}')
    lock.release()

def workerB():
    '''this worker will access the global counter to decrement it'''
    global counter
    lock.acquire() # we have exclusive access to the lock (when it becomes available)
    while counter > -10:
        counter-=1
        print(f'Worker B decrements the counter to {counter}')
    lock.release()

if __name__ == '__main__':
    # workerA()
    # workerB()
    t1 = threading.Thread(target=workerA)
    t2 = threading.Thread(target=workerB)
    t1.start()
    t2.start()
    t1.join()
    t2.join()