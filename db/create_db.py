import sqlite3 # this database is part of the python standard library

def accessDB():
    '''create a database then add a table to it'''
    conn = sqlite3.connect('my_db') # either create or else open this database
    curs = conn.cursor() # this is the database access mechanism
    # we need an SQL statement (note the round brackets)
    st = '''
    CREATE TABLE zoo
    (
        creature VARCHAR(32) PRIMARY KEY,
        count int,
        cost float
    )
'''
    try:
        curs.execute(st)
        conn.commit()
        conn.close() # tidy up
    except Exception as e:
        print(e)

if __name__ == '__main__':
    accessDB() # run this ONCE to create DB and a table