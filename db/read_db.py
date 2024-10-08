import sqlite3

def readDB():
    '''commit one data member to the database'''
    conn = sqlite3.connect('my_db') # connect to our database
    curs = conn.cursor()
    # sql statement
    st = '''
    SELECT * FROM zoo
'''
    try:
        curs.execute(st)
        conn.commit()
        # we can now read back any resulting data
        rows = curs.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print(e)

if __name__ == '__main__':
    r = readDB()
    print(r, type(r))