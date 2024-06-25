#!/usr/bin/python3

""" script that lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    try:
        db = MySQLdb.connect(
            host="localhost",
            password=password,
            user=username,
            database=dbname,
            port=3306
            )
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        myresult = cur.fetchall()
        for row in myresult:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error {e}")
        sys.exit(1)
