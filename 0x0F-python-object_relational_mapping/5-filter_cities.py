#!/usr/bin/python3
"""
List all cities of a state
"""
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    db = MySQLdb.connect(user=user, passwd=passwd, db=db, port=3306)

    cur = db.cursor()
    state_name = sys.argv[4]
    query = """
    SELECT cities.name
    FROM cities
    JOIN states
    ON cities.state_id = states.id
    WHERE states.name = %s
    """
    cur.execute(query, (state_name,))
    cities = cur.fetchall()

    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    cur.close()
    db.close()
