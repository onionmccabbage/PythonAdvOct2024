from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

# invoke pyest like this:
# python -m pytest -v using_pytest.py

def testDefaults():
    '''using no parameters should invoke the defaults'''
    tA = Task() # use all the defaults
    tC = Task(None, None, False, None)
    assert tA == tC # this is a pyset assertion
    # tB = Task('Learn testing', 'Deidre', False, 1)

if __name__ == '__main__':
    '''use our named tuple'''
    
    # print(tA, tB, type(tA))
