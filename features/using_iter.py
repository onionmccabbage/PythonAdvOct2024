# we can choose to make anything iterable using iter

class Evens:
    '''this class will iterate over a set of even numbers'''
    def __init__(self, limit):
        self.__limit = limit
        self.__start = 0
    def __iter__(self):
        '''to make any class iterable simply implement or override __iter__'''
        return self # easy as that!!
    def __next__(self):
        '''once the class is iterable wel also implement or override __next__'''
        if self.__start > self.__limit:
            raise StopIteration # our iterator is exhausted
        else:
            rval = self.__start
            self.__start +=2
            return rval 
        
def main():
    '''execise the code'''
    e = Evens(100) # an instance of our iterable class
    print( e.__next__() ) # 0
    print( e.__next__() ) # 2
    print( e.__next__() ) # 4
    for _ in e:
        print(f'Next even value is {_}')

if __name__ == '__main__':
    main()