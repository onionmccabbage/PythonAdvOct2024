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
        fout.close() # tidy up
    except Exception as e:
        print(e)

if __name__ == '__main__':
    txt = 'Here is a lot of text to be written to a file'
    writeToFile(txt)
    