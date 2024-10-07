# we need our function to behave differently depending on how many arguments are passed
# This is similar to overloading in other languages

def simOverload(*args):
    '''if there is one argument, return it as an absolute value 
    For two args, add them
    For three, multiply them all together'''
    if len(args)==1:
        return abs(args[0])
    elif len(args)==2:
        return args[0]+args[1]
    elif len(args)==3:
        return args[0]*args[1]*args[2]
    
if __name__ == '__main__':
    print( simOverload(-99) )
    print( simOverload(-99, -88) )
    print( simOverload(-99, 3, 2) )