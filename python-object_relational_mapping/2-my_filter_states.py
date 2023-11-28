#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Check if all 4 arguments are provided
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(argv[0]))
        exit(1)

    # Extract command-line arguments
    username, password, database, state_name = argv[1], argv[2], argv[3], argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query with the provided state_name
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

