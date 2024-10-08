# by default all standard output is sent to the console
import sys

class RedirectOut():
    '''Redirect output to a different stream, then recover the original stream'''
    def __init__(self, new_stdout):
        self.stdout = new_stdout
    def __enter__(self):
        '''the __enter__ method runs whenever this class or an instance is run'''
        self.orig_stdout = sys.stdout
        sys.stdout = self.stdout # all output will be directed to this new stream
    # Careful - __exit__ MUST be given some default parameters
    def __exit__(self,  exc_type, exc_value, exc_traceback):
        ''' the __exit__ method is invoked whenever the class or an instance finishes'''
        sys.stdout = self.orig_stdout # recover the original stream

if __name__ == '__main__':
    with open('my_log.txt', 'a') as fobj:
        r = RedirectOut(fobj) # an instance of our class, passing in the file access object
        with r:
            print('this will end up in our text file')
        # when the with ends, we are back to normal
        print('normal service resumed')
    # at this point, the first 'with' ends
        