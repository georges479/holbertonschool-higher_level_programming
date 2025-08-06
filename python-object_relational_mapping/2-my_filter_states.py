#!/usr/bin/python3
"""
Lists all values in the states table where name matches the argument.
Usage: ./2-my_filter_states.py <mysql username>
<mysql password> <database name> <state name searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()

    # Create SQL query using format (as required by instructions)
    query = "SELECT * FROM states WHERE name = \
    '{}' ORDER BY id ASC".format(sys.argv[4])

    cursor.execute(query)

    # Fetch and print results
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
