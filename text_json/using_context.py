from contextlib import contextmanager
import sys

@contextmanager # make this funtion behave as a context manager
def outputRedirect(newOutput):
    '''redirect the default print output (sys.stdout)'''
    old_stdout = sys.stdout # remember the current standard output
    sys.stdout = newOutput
    yield # our function will yield the next available object to be written to a stream
    sys.stdout = old_stdout # set things back to how they were before

if __name__ == '__main__':
    # first check the existing sys.stdout
    sys.stdout.write('This stream is output by the default sys.stdout') # same as calling print()
    with open('my_stream.txt', 'a') as fobj: # we now have a file access object
        with outputRedirect(obj):
            print('This will be written to our file')
            sys.stdout.write('...more file output')
    print('back to the normal output')