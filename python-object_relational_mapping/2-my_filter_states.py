#!/usr/bin/python3
"""
Displays all states from the database hbtn_0e_0_usa
whose name matches the argument provided (case-sensitive).

Usage:
    ./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name searched>

Connects to the MySQL database and fetches states
with a name exactly matching the provided argument.
"""

import sys
import MySQLdb


def main():
    """Connect to the database and print states matching the name argument."""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = ("SELECT * FROM `states` WHERE BINARY `name` = %s")
    cursor.execute(query, (sys.argv[4],))
    states = cursor.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    main()
