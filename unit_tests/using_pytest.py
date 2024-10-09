from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

if __name__ == '__main__':
    '''use our named tuple'''
    tA = Task() # use all the defaults
    tB = Task('Learn testing', 'Deidre', False, 1)
    print(tA, tB, type(tA))