#!/usr/bin/python3
"""lists all cities of a state given by user"""

import MySQLdb
import sys

if __name__ == "__main__":
    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    query = """SELECT cities.name FROM cities INNER JOIN
                states ON states.id=cities.state_id WHERE states.name = %s"""
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
