#!/usr/bin/python3
""" script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument """

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM states WHERE BINARY name = '{}'\
                ORDER BY id ASC".format(sys.argv[4]))
        for row in cur.fetchall():
            print(row)

    conn.close()
