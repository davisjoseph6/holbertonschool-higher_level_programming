#!/usr/bin/python3
import MySQLdb
import sys

if len(sys.argv) != 4:
    print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
    sys.exit(1)

username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

# Connect to the MySQL server
db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

# Create a cursor object to execute queries
cursor = db.cursor()

# Execute the query to select all states and order by id
query = "SELECT * FROM states ORDER BY id;"
cursor.execute(query)

# Fetch all the rows
rows = cursor.fetchall()

# Display the results
for row in rows:
    print(row)

# Close the cursor and database connection
cursor.close()
db.close()
