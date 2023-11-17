#!/usr/bin/python3
"""Safe from MySQL injections"""

import MySQLdb
import sys

if __name__ == "__main__":
    states_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    que = "SELECT * FROM states WHERE name LIKE %s ORDER BY states.id"
    cur.execute(que, (states_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
