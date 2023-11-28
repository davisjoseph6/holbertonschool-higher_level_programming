#!/usr/bin/python3
"Lists all cities"

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    datab = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=passwd, db=datab)
    cur = db.cursor()

    cur.execute(
        """SELECT cities.id, cities.name, states.name FROM cities
        INNER JOIN states ON cities.state_id = states.id
        ORDER BY cities.id""")

    results = cur.fetchall()
    for result in results:
        print(result)

    cur.close()
    db.close()
