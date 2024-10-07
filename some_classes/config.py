# here we attempt to configure a figure with default properties 
# or else properties from the user

import sys # this gives access to the system on which Python is running
from figure import Figure

if __name__ == '__main__':
    # sys.argv[0] is ALWAYS the name of the current running module
    print(sys.argv) # the system argument variables is a list of arguments
    if len(sys.argv) > 1: # we may pass additional system argumnent variables
        '''use additional arguments for values in our figure class'''
        # CAREFUL - all sys.argv members are STRINGS
        num_sides = int(float(sys.argv[1]))
        size = float(sys.argv[2])
        colour = sys.argv[3]
        name = sys.argv[4]
    else: # if no suitable values weree provided, ask the user
        # CAREFUL - remember 'input' is ALWAYS a string
        num_sides = int(float(input('How many sides? ')))
        size = float(input('Figure size? '))
        colour = input('Colour? ')
        name = input('Name? ')
    # construct an instance
    my_fig = Figure(num_sides, size, colour, name)
    print(my_fig)