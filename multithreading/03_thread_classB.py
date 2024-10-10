from threading import Thread
import time
import timeit # this is a more accurate library for measuring time differences
import random # emulate long-running processes by sleeping for random amount of time

class MyClassB(): # here we do not inherit from Thread
    '''To call a class as a thread we implement a __call__ method'''
    def __init__(self):
        pass
    def __call__(self, n):
        '''__call__ lets us invoke this class on a thread'''
        msg = ''
        for _ in range(0,10):
            msg += f'{n} is sleeping...'
            time.sleep(random.random()*0.1)
        # print(msg) # try to minimize I/O

def main():
    ''' we may invoke our class as a thread'''
    cA = MyClassB()
    print('on the main thread')
    thread_l = []
    # we may be interested in the overall time ths itakes
    # start = time.time() # the time library is ok but...
    start = timeit.default_timer() # a more accurate utility for delta-time
    
    # how many threads are actually available? Depends on the system and what else is running
    for _ in range(0,32): # the OS will manage a pool of threads, queuing and recycling threadds as needed
        # we may target an instance of a class which implements __call__
        thread_l.append(Thread(target=cA, args=(_,)))
        # CAREFUL - no point start-join each thread here, that would be procedural
    # print('main thread has spawned several child threads')
    # we may start our threads
    for _ in thread_l:
        _.start()
    # we may join out threads
    for _ in thread_l:
        _.join()
    # end = time.time()
    end = timeit.default_timer()
    print(f'Overall time is {end-start}')

if __name__ == '__main__':
    main()