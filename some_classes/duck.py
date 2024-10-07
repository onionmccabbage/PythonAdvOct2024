# sometimes we need properties and methods that belong to the class itself (rather than to any instances of the class)

class Duck():
    count = 0 # this property belongs to the class
    def __init__(self, n):
        self.__n = n # we do not use a setter to validate
        Duck.count += 1 # every new duck instance will increment this count
    # we may also like to have a method that belongs to the class
    @classmethod # a decorator
    def howMany(cls): # cls is the conventional name forthe class itself
        return f'The Duck class has {cls.count} instances'


if __name__ == '__main__':
    d1 = Duck('Howard')
    print(Duck.count) # 1
    d2 = Duck('Mallard')
    print(Duck.count) # 2
    d3 = Duck('Eider')
    print(Duck.count) # 3
    # duck-typing... if it looks ike a duck, walks like a duck, its probably a duck
    d99 = {'n':'Roast'} # this is like a Duck instance, so Python considers it to be a Duck instance
    print( Duck.howMany() )  # 3
