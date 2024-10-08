import sqlite3

def customRead(w):
    '''retrieve a specific member fro mthe database'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st = f'''
    SELECT creature, count, cost FROM zoo
    WHERE creature LIKE "%{w}%"
'''
    try:
        curs.execute(st)
        conn.commit()
        rows = curs.fetchall()
        conn.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    w = input('Which creature? ')
    r = customRead(w)
    print(r)
