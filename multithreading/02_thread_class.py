from threading import Thread
import time
import random # we will sleep for random times

class MyClass(Thread): # we inherit from the Thread class
    '''Any class may inherit from Thread'''
    def __init__(self, n, x):
        # call the __init__ of the parent class (Thread)
        # super().__init__(group, target, name, args, kwargs, daemon=daemon) # we tend to avoid this!!
        # super().__init__() # NB we do not pass self
        Thread.__init__(self)
        self.n = n # we could use @property setter/getter functions
        self.x = x
    # we override the run method of Thread
    def run(self):
        '''When this class is invoked, the run method will execute it on a new thread'''
        for _ in range(0,10): # on average, this class will run for 0.5 sec
            print(f'{self.n} is sleeping')
            time.sleep(random.random()*0.1) # sleep for up to 0.1 second

if __name__ == '__main__':
    print('On the main thread')
    tA = MyClass('A', True)
    tB = MyClass('B', [])
    tC = MyClass('C', (3,2,1))
    tD = MyClass('D', 'data')
    tE = MyClass('E', {'A', True, 44, None})
    print('Starting the thread classes')
    tA.start()
    tB.start()
    tC.start()
    tD.start()
    tE.start()
    # we usually wait for the threads to rejoin
    tA.join()
    tB.join()
    tC.join()
    tD.join()
    tE.join()
    print('where is this printed.....')