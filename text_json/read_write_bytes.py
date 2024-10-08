# storing data as bytes is usually more efficient
# text files need an encoding, bytes are simply stored as-is

def writeBytes(b):
    '''write some bytes to a file'''
    # we should use try-except
    with open('bfile', 'wb') as fout: # wb will (over)write bytes
        fout.write(b) # no need to close()

def readBytes():
    '''retrieve bytes from a file'''
    # we should use try-except
    with open('bfile', 'rb') as fin:
        retrieved = fin.read()
    return retrieved

def makeBytes(v):
    '''convert v to bytes'''
    b = bytes(v)
    return b

if __name__ == '__main__':
    # some byte data
    b1 = b'this will be a byte object'
    b2 = bytes('more byte data', 'utf8') # UTF8 is good for most cases
    print(type(b1), type(b2)) # we have byte objects
    # make some bytes out of a range of values
    v = range(0,255)
    b3 = makeBytes(v)
    writeBytes(b3)
    # writeBytes(b2)
    # now we read back the bytefile contents
    b4 = readBytes() # we should have bytes
    s = f'{b4}' # attempt to convert the bytes to text
    print(s)
    # other ways
    b5 = 'this is plain text \n'.encode('utf16')
    writeBytes(b5)
    b6 = readBytes()
    s2 = b6.decode()
    print(s2)