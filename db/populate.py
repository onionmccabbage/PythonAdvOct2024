import sqlite3

def populateDB(creatures_t):
    '''commit many valid data members to the database'''
    conn = sqlite3.connect('my_db') # connect to our database
    curs = conn.cursor()
    # sql statement
    st = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
'''
    for item in creatures_t:
        try:
            # check the data members are sane and valid
            if type(item['creature'])==str:
                n = item['creature'] # read a member from the dictionary
            else:
                raise Exception('Creature name must be a string')
            if type(item['count'])==int:
                count = item['count']
            else:
                raise Exception('Creature count must be an integer')
            if type(item['cost']) in (float, int):
                cost = item['cost']
            else:
                raise Exception('Creature cost must be a float or int')
            curs.execute(st, (n,count, cost)) # here we replace ?,?,? with sanitized values
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    creatures_t = ( # normally this comes from JSON or API etc.
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    ) 
    populateDB(creatures_t)