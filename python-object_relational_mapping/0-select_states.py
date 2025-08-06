#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.

Usage:
    ./0-select_states.py <mysql username> <mysql password> <database name>

This script connects to a MySQL database using credentials
provided as command-line arguments, then fetches and prints
all rows from the 'states' table.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database using command line arguments
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    
    # Execute SQL query to select all data from states table
    cursor.execute("SELECT * FROM `states`")
    
    # Fetch all results and print each state
    states = cursor.fetchall()
    for state in states:
        print(state)
