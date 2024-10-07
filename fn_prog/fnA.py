# every function may take positional and keyword arguments

def myFn(x, y=3):
    '''x is a positional argument, y is a keyword argument'''
    return (x,y) # a tuple

#single asterisk * will gather together positional arguments
#double asterisk ** will gather together keyword arguents
def doStuff(*args, **kwargs): # arg and kwarg are simply conventions
    return args, kwargs # a tuple and a dict

if __name__ == '__main__':
    print( myFn(4) ) # x is 4, y is default 
    print( myFn(y=2, x=99) ) # both as keyword arguments
    print( myFn(-4, -3) ) # both as positional arguments
    # using args and kwargs
    print( doStuff(5,2,6,8,6,3,2,True,[], (5,4,3)) ) # all positional args
    print( doStuff(x=88, b=False, T=('a',), d={}) )  # all as kwargs
    # NB positionals must come before any kwargs