from inherit import AbstractShape

# If we choose we may specify slots. 
# They will determine which mangled properties we allow in our class

class Shape(AbstractShape): # we choose to inherit from our ABC
    '''It is a good idea to document your coee using docstring like this
    This class captures the number of sides, size and colour of a shape'''
    # delcare slots for the mangled properties of this class
    __slots__ = ('__num_sides', ) # a tuple
    def __init__(self, num_sides) -> None: # here is an annotation reminding us this method will return nothing
        '''the __init__ method is similar to a constructor
        it will run once every time we make an instance of this class'''
        # this will call our num_sides setter method
        self.num_sides = num_sides # we set initial properties in the __init__ method
        self.__coffee = 'broken'
    @property # this is a decorator (begins with @)
    def num_sides(self):
        '''return the name-mangled property (a bit like private properties)'''
        return self.__num_sides
    @num_sides.setter # called when we write self.num_sides = num_sides
    def num_sides(self, num_sides):
        '''here we may validate it is a positive integer'''
        if type(num_sides)==int and num_sides>0:
            self.__num_sides = num_sides # set the name-mangled property
        else: # what to do if the num_sides is invalid
            raise TypeError('Number of sides must be a positive integer')
    #our abstract base class insists that we implement a __str__ method
    def __str__(self): # remember - __str__ will be used by print()
        return f'Shape with {self.num_sides} sides' # calls the num_sides getter method

def main():
    '''call this function'''
    '''make instances of our class'''
    try:
        s1 = Shape(3) # this will invoke the __init__ method once
    except TypeError as te:
        print(f'Problem: {te}') # return a helpful message
    # can we add additional mangled members?
    s1.__coffee = 'broken'
    print(s1) # this will invoke the __str__ method of our class


if __name__ == '__main__':
    main() # this is a common architecture