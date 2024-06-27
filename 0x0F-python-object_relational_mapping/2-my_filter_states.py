#!/usr/bin/python3
"""script that takes in an argument and displays all values
in the states able of hbtn_0e_0_usa where name matches
the argument"""


import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
                host="localhost",
                user=username,
                password=password,
                database=dbname,
                port=3306,
                charset="utf8"
                )
        cur = db.cursor()
        cur.execute("""
        SELECT *
        FROM states
        WHERE name LIKE BINARY '{}'
        ORDER BY id ASC
        """.format(state_name))
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)
