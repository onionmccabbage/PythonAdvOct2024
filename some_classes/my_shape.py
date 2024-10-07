from inherit import AbstractShape

class Shape(AbstractShape): # we choose to inherit from our ABC
    '''It is a good idea to document your coee using docstring like this
    This class captures the number of sides, size and colour of a shape'''
    def __init__(self, num_sides) -> None: # here is an annotation reminding us this method will return nothing
        '''the __init__ method is similar to a constructor
        it will run once every time we make an instance of this class'''
        # this will call our num_sides setter method
        self.num_sides = num_sides # we set initial properties in the __init__ method
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





if __name__ == '__main__':
    '''make instances of our class'''
    s1 = Shape(3) # this will invoke the __init__ method once