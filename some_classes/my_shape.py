from inherit import AbstractShape

class Shape(AbstractShape): # we choose to inherit from our ABC
    '''It is a good idea to document your coee using docstring like this
    This class captures the number of sides, size and colour of a shape'''
    def __init__(self, num_sides) -> None: # here is an annotation reminding us this method will return nothing
        '''the __init__ method is similar to a constructor
        it will run once every time we make an instance of this class'''
        self.num_sides = num_sides # we set initial properties in the __init__ method


if __name__ == '__main__':
    '''make instances of our class'''
    s1 = Shape(3) # this will invoke the __init__ method once