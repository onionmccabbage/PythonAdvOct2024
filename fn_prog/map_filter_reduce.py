import util # we now have access to all the utility functions
# reduce is part of the functools library
import functools

def isOdd(w):
    return w%2 != 0 # we are assuming these are integers

def main():
    '''use map, filter and reduce'''
    powers = map(util.raiseToPower, range(1,10))
    print(powers) # we have a map object
    # we may choose to pull out the next available value from our map object
    print( powers.__next__() ) # 1
    print( powers.__next__() ) # 4
    print('----------')
    for _ in powers:
        print(_)

    # in a similar way, we can use 'filter' to return members that match a criteria
    odd_nums = filter(isOdd, range(0,100)) # NB we need True or False
    # we can use 'reduce' to iteratively apply a function to return a cumulative single result
    print(odd_nums) # we have a filter object
    print( odd_nums.__next__() ) # 1
    print( odd_nums.__next__() ) # 3
    print( odd_nums.__next__() ) # 5
    print( odd_nums.__next__() ) # 7
    print('----------')
    for _ in odd_nums:
        print(_, end=', ')

    # there are no nore values in the filter object, so we cannot see any more results
    total = functools.reduce( util.addThem, range(1,11) ) # 55
    print(total)

if __name__ == '__main__':
    main()