#!/usr/bin/python3
"""
Lists al values in the states tables of a database where name
matches the argumenti in safe way to avoid sql injections
"""
import sys
import MySQLdb
if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    db = MySQLdb.connect(user=user, passwd=passwd, db=db, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s;", (sys.argv[4],))
    states = cur.fetchall()
    for state in states:
        print(state)
# Hassan Munene
