#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.

Usage:
    ./0-select_states.py <mysql username> <mysql password> <database name>

Connects to the MySQL database and prints all rows in the 'states' table.
"""

import sys
import MySQLdb


def main():
    """Connect to the database and print all states."""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states`")
    states = cursor.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    main()
