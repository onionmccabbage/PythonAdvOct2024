# this figure class will inherit eeveryting from the shape class
# we then add a 'name' property
from my_shape import Shape

class Figure(Shape):
    '''All the properties and methods of Shape are now available to us. We typically call the __init__ of Shape
    We will also have a property for 'name' '''
    def __init__(self, num_sides, size, colour, name) -> None:
        super().__init__(num_sides, size, colour)
        self.name = name
    @property
    def name(self):
        return self.__name # using name-mangling is a really good idea - a bit like private properties
    @name.setter
    def name(self, name):
        if type(name)==str and name !='':
            self.__name  = name
        else:
            raise TypeError('Name must be a non-empty string')
    # we might choose to write additonal methods, e.g. tp derive values (e.g. area) from the properties
    # we can override methods from the parent with our own methods
    def __str__(self) -> str:
        '''within a class we MUST refer to 'self' to access class methods'''
        return  self.doText() + f' and is {self.colour} size {self.size}'
    def doText(self):
        '''return info about this class'''
        return f'{self.name} has {self.num_sides} sides'

if __name__ == '__main__':
    f1 = Figure(5, 3.2, 'red', 'pentagon')
    # we can mutate properties by calling the setter-method of a class as if it is a property
    f1.size = 4.5 # the setter method will validate this property
    print(f1) # use the __str__ method
