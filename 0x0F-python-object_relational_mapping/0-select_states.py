#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys


def list_states(my_name, my_pass, my_data):
    """function to list states
    args
    """
    try:
        # connect to mysql server
        db = MySQLdb.connect(host="localhost", port=3306, user=my_name,
                             password=my_pass, database=my_data)
        # query sql
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        # get results
        rows = cursor.fetchall()
        # print result
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        # Close all cursors
        cursor.close()
        # close all databases
        db.close()


if __name__ == " __main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    # Get MySql credentials from the cli
    my_name, my_pass, my_data = sys.argv[1:4]
    # call function to list states
    list_states(my_name, my_pass, my_data)
