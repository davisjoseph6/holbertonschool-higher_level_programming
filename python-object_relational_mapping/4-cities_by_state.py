#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa  """

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    with conn.cursor() as cur:
        cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")

        for row in cur.fetchall():
            print(row)

    conn.close()
