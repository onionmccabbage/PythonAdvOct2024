# storing data as bytes is usually more efficient
# text files need an encoding, bytes are simply stored as-is

def writeBytes(b):
    '''write some bytes to a file'''
    # we should use try-except
    with open('bfile', 'wb') as fout: # wb will (over)write bytes
        fout.write(b) # no need to close()

def readBytes():
    '''retrieve bytes from a file'''


if __name__ == '__main__':
    # some byte data
    b1 = b'this will be a byte object'
    b2 = bytes('more byte data', 'utf8') # UTF8 is good for most cases
    print(type(b1), type(b2)) # we have byte objects
    writeBytes(b1)
    # writeBytes(b2)