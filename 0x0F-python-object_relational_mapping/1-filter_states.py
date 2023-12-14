#!/usr/bin/python3


import sys
import MySQLdb

if __name__ == "__main__":

    db_conn = MySQLdb.connect(user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3],
                              host='localhost',
                              port=3306)

    cur = db_conn.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db_conn.close()
