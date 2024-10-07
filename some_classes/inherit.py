# abc is an Abstract Base Class
from abc import ABCMeta, abstractmethod
# ABC is entirely optional - you may never need to use it

# in Python EVERYTHING is an object - including modules, functions and classes

class A: # this implicitly inherists from Object
    pass

class B(): # also implicitly inherits from Object
    pass

class C(object): # explicitly inherit from object
    pass

class D(dict): # inherit from dictionary
    pass

# Using ABC - we can declare our own abscract classes
# this is like a class template - all the child cl;asses must look like this
# NB we NEVER make instances of an abstract class, we only everr inherit from them
class AbstractShape(metaclass=ABCMeta): # we now have our own abstract base class
    '''Abstraction means we can declare properties and methods we will need in actual classes'''
    @property # we may declare abstract properties for this class
    @abstractmethod
    def num_sides(self, num_sides):
        pass
    @abstractmethod
    # we may choose to indicate a return type
    def __str__(self) -> str: # remember - all classes will use __str__ when printed
        '''this function will be used by print()'''
        # we NEVER write any concrete code in an abstract base class

