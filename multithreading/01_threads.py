from threading import Thread
import time # we will sleep to represent long-running functionality

# any function may be invoked on a separate thread
def myFn(n):
    '''this is a normal function, just like any other'''
    time.sleep( 1 ) # sleep for one second
    print(f'this is the function: {n}')

if __name__ == '__main__':
    # we may invoke the function in the normal way (procedurally)
    # myFn(1)
    # myFn(5)
    # myFn(3)
    # myFn(2)
    # myFn(4)
    tA = Thread(target=myFn,  args=('A',)) # a one-member tuple
    tB = Thread(target=myFn,  args=('B',)) 
    tC = Thread(target=myFn,  args=('C',)) 
    tD = Thread(target=myFn,  args=('D',)) 
    tE = Thread(target=myFn,  args=('E',)) 
    print('on the main thread')
    tB.start() # these threads can run concurrently
    tD.start()
    tE.start()
    tC.start()
    tA.start() # at this point the function will start execution on a separate thread
    print('still on the main thread')
    tA.join() # block the main thread until tA re-joins
    tB.join()
    tC.join()
    tD.join()
    tE.join()
    print('when does this get printed....') # main thread continues when the other threads have (re)joined