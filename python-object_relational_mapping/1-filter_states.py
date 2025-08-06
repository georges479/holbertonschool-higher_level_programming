#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa.

Usage:
    ./1-filter_states.py <mysql username> <mysql password> <database name>

Connects to the MySQL database, fetches all states ordered by id,
and prints those whose name starts with the letter 'N'.
"""

import sys
import MySQLdb


def main():
    """Connect to the database and print states starting with 'N'."""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")
    states = cursor.fetchall()
    for state in states:
        if state[1].startswith('N'):
            print(state)


if __name__ == "__main__":
    main()
