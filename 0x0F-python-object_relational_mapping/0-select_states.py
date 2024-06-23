#!/usr/bin/python3


import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect (
            host="localhost",
            password="root",
            user="root",
            database="hbtn_0e_0_usa",
            port=3306
            )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    myresult = cur.fetchall()
    for row in myresult:
        print(row)
    cur.close()
    db.close()
