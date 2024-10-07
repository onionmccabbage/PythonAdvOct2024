# here we write a custom decorator which can reveal the args/kwargs of ANY function

def showArgs(f):
    '''This is a higher-order function. It takes a function object as an argument
    We will reveal any positional arguments and any keyword arguments 
    before running the passed-in function'''
    def newFunc(*args, **kwargs):
        txt = f'''Running function called {f.__name__}
The positional arguments are {args}
the keyword arguments are {kwargs}
'''
        print(txt) # output what we have introspected
        # finally we run the original function
        return f(*args, **kwargs) # include all original aruments
    return newFunc # we do not invoke this new function

