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
    # we can override methods from the parent with our own methods
    def __str__(self) -> str:
        return f'{self.name} has {self.num_sides} sides, and is {self.colour} size {self.size}'

if __name__ == '__main__':
    f1 = Figure(5, 3.2, 'red', 'pentagon')
    print(f1) # use the __str__ method
