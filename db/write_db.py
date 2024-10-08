import sqlite3

def writeDB():
    '''commit one data member to the database'''
    conn = sqlite3.connect('my_db') # connect to our database
    curs = conn.cursor()
    # sql statement
    st = '''
    INSERT INTO zoo
    VALUES ("Penguin", 16, 0.52)
'''
    try:
        curs.execute(st)
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    writeDB()