#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    db = MySQLdb.connect(user=user, passwd=passwd, db=db, port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id;")
    states = cur.fetchall()
    for state in states:
        print(state)

# hassan Munene
