#!/usr/bin/python3

"""
    Script Extract All row of data(data)
    from state Table If Exist
    parameterized queries to prevent SQLi
    (args) are received from sys.argv
"""


import sys
import MySQLdb


if __name__ == "__main__":

    db_conn = MySQLdb.connect(user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3],
                              host='localhost',
                              port=3306)

    state = sys.argv[4]
    cur = db_conn.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state,))

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db_conn.close()
