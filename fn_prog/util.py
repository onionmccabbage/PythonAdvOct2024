from introspect import showArgs

@showArgs
def raiseToPower(m,n=2):
    '''raise m to the power of n'''
    return m**n

@showArgs
def squareIt(a):
    '''return the square of a'''
    return a*a

@showArgs
def addThem(p, q):
    '''add them'''
    return p+q

if __name__ == '__main__':
    print( raiseToPower(3,7) )
    print( raiseToPower(3,n=7) )
    print( raiseToPower(m=3,n=7) )
    print( squareIt(4) )
    print( addThem(-5,-2) )