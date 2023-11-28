#!/usr/bin/python3
"""Script that lists all states with a name starting with N (upper N)"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username, password, database = sys.argv[1:]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute the SQL query to select states with names starting with 'N'
    query = """
            SELECT * FROM states
            WHERE name LIKE 'N%'
            ORDER BY id;
            """
    cur.execute(query)

    # Fetch all the rows
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()

