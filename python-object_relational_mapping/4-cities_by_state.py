#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    if len(sys.argv) != 4:
        sys.exit('Use: 4-cities_by_state.py<mysql username> <mysql password>'
                 ' <database name>')

    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT ct.id, ct.name, st.name\
                    FROM cities as ct\
                    INNER JOIN states as st\
                    ON ct.state_id = st.id ORDER BY id")
    query_rows = cur.fetchall()
    for city in query_rows:
        print(city)
    cur.close()
    conn.close()
