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

# some other DB conn mechanisms
# see https://wiki.python.org/moin/DatabaseInterfaces
# DB2
# import DB2 # remember to pip install first!!
# conn = DB2.connect(dsn='ibm-DB', uid='analyst', pwd='db2pwd')

# Sybase
# import Sybase
# conn = Sybase.connect('SYBASE', 'username', 'passwd', 'databasename')

# Oracle
# import cx_Oracle
# conn = cx_Oracle.connect('username', 'passwd', 'hostname:port/SID')
# conn2 = cx_Oracle.connect('username/passwd@hostname:portno/SID')
# dsn_tns = cx_Oracle.makedsn('hostname', portno, 'SID')
# conn3 = cx_Oracle.connect('username', 'passwd', dsn_tns)

# MySQL
# import MySQLdb
# conn = MySQLdb.connect(host = "hostname", user = "username",
# passwd = "password", db = "dbname")

# PySQLite
# from pysqlite2 import dbapi2 as sqlite
# conn = sqlite.connect("mydb", connectionproperties)

# ODBC
# import odbc
# conn = odbc. odbc("myDSN/username/password")

