#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa, ordered by city id.

Usage:
    ./4-cities_by_state.py <mysql username> <mysql password> <database name>

Connects to the MySQL database, fetches city id, city name,
and state name by joining cities and states tables,
then prints each city record ordered by city id.
"""

import sys
import MySQLdb


def main():
    """Connect to the database and print all cities ordered by city id."""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = ("SELECT c.id, c.name, s.name "
             "FROM cities AS c "
             "INNER JOIN states AS s ON c.state_id = s.id "
             "ORDER BY c.id")
    cursor.execute(query)
    cities = cursor.fetchall()
    for city in cities:
        print(city)


if __name__ == "__main__":
    main()
