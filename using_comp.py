# generators are part of python
def genSquares(n=0, stop=10, step=1):
    '''generate the squares from n to stop every step'''
    count = n
    stop_at = stop-1 # follow Python convention
    while count < stop_at:
        count += step
        yield count **2 # yield will continue to yield values

if __name__ == '__main__':
    # the members of a generator are created on demand - they do NOT perist in memory
    odds = (i for i in range(1,11,2)) # a generator
    # obviously a list must exist entirely in memory
    evens = [i for i in range(0,11,2)] # a list
    print(type(odds), type(evens))
    for _ in odds:
        print(_, end=', ')
    for _ in evens:
        print(_, end=', ')
    # make use of our custom generator
    s = genSquares()
    print(type(s))
    # we can call __next__()
    print( s.__next__() ) # 1
    print( s.__next__() ) # 4
    print('---------------')
    for _ in s:
        print(_)
    # print( s.__next__() ) # this should fail, the generator has been exhausted
