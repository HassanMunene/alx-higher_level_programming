#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument provided.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    db = MySQLdb.connect(user=user, passwd=passwd, db=db, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS = '{}';".format(sys.argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
# hassan Munene
