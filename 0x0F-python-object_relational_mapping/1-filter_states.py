#!/usr/bin/python3
"""script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa"""


import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(
                host="localhost",
                user=username,
                password=password,
                database=database,
                port=3306,
                charset="utf8"
                )
        cur = db.cursor()
        cur.execute("""
        SELECT *
        FROM states
        WHERE name Like BINARY 'N%'
        ORDER BY states.id ASC
        """)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)
    cur.close()
    db.close()
