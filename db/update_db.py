import sqlite3

def customUpdate(w):
    '''update the database'''
    q = int(float(w['count'])) # the new 'count'
    a = w['creature']
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st = f'''
    UPDATE zoo
    SET count={q}
    WHERE creature = "{a}"
'''
    try:
        curs.execute(st)
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    creature = input('Which creature? ')
    q = input('How many? ') # remember - input is ALWAYS a string
    obj = {'creature':creature, 'count':q} # we could also handle cost
    customUpdate(obj)