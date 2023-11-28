#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa  """

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    with conn.cursor() as cur:
        sql_inject = "SELECT cities.name \
                 FROM cities \
                 INNER JOIN states \
                 ON states.id = cities.state_id \
                 WHERE states.name = %s \
                 ORDER BY cities.id"

        cur.execute(sql_inject, (sys.argv[4],))

        cities_list = [row[0] for row in cur.fetchall()]
        cities_str = ", ".join(cities_list)
        print(cities_str)

    conn.close()
