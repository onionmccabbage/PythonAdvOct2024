import util # we now have access to all the utility functions

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
    odd_nums = filter(isOdd, range(0,100))
    print(odd_nums) # .....?

if __name__ == '__main__':
    main()