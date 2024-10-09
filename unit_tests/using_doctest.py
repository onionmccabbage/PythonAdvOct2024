import doctest # we can write doctests within the documentation string

def nthPower(d=2, p=4):
    '''return the pth power pf d i.e d**p
    We can write doctests here, within the docstring
    >>> nthPower()
    16
    >>> nthPower(4,p=3)
    64
    '''
    return d**p

def cubeIt(a,b):
    '''return the cube of all numbers from a to b
    >>> cubeIt(3, 8)
    [27, 64, 125, 216, 343]
    >>> cubeIt(1,101) # doctest:+ELLIPSIS
    [1, 8, ..., 1000000]
    '''
    answers = []
    for i in range(a,b):
        answers.append( i**3 )
    return answers

# doctest is a really good reason to use if __name__ ==...
if __name__ =='__main__':
    # print( nthPower() )
    doctest.testmod(verbose=True) # we could redirect the output to a test log file
    # print( cubeIt(-3, 4) )