#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
where name matches the argument (safe from SQL injections).

Usage:
    ./2-my_filter_states.py <mysql username> <mysql password>
    <database name> <state name searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()

    # SQL query with placeholders to avoid SQL injection
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (sys.argv[4],)
    )

    # Print matching states
    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
