def writeToFile(t):
    '''use a file access object to commit text to a file'''
    try:
        fout = open('my_log.txt', 'at')
        size = len(t)
        offset = 0
        chunk = 12
        while True:
            if offset > size:
                fout.write('\n') # terminate the output with a new line
                break # stop the while loop
            else:
                part = t[offset:offset+chunk] # [start:stop-before]
                fout.write(part) # commit these characters to the file
                offset += chunk
        fout.close() # tidy up
    except Exception as e:
        print(e)

def seekContent(n=18):
    '''seek to specific content within a text file'''
    try:
        fin = open('my_log.txt', 'rt')
        fin.seek(n) # move the file cursor to the position n
        the_rest = fin.read()
        fin.close()
        return the_rest
    except Exception as e:
        print(e)


if __name__ == '__main__':
    txt = 'Here is a lot of text to be written to a file'
    writeToFile(txt)
    print( seekContent(42) )
    