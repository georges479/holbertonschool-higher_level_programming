#!/usr/bin/python3
"""
Displays all cities of a given state from the database hbtn_0e_4_usa.

Safe from SQL injections by using parameterized queries.

Usage:
    ./5-filter_cities.py <mysql username> <mysql password> <database name> <state name>
"""

import sys
import MySQLdb


def main():
    """Connect to the database and print all cities of the given state."""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = ("SELECT c.name "
             "FROM cities AS c "
             "INNER JOIN states AS s ON c.state_id = s.id "
             "WHERE s.name = %s "
             "ORDER BY c.id")
    cursor.execute(query, (sys.argv[4],))
    cities = cursor.fetchall()
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))


if __name__ == "__main__":
    main()
